# -*- coding: utf-8 -*-
import logging
import constants
from stream import StreamClientManager
from schemas.nats import NatsChatMessage, NatsChatMessageAttachment, ChatOptional
from schemas.nats import Messaging as FacebookMessaging
from schemas.chat_message_schema import FacebookIncomingMessage


stream_client_manager = StreamClientManager()
logger = logging.getLogger(constants.SOP_LOGGER_NAME)


# -----------------------------------------------------------------------
#   Facebook
# -----------------------------------------------------------------------
async def facebook_create_nats_chat_message(
    entry_id: str,
    messaging: FacebookMessaging,
    chat_type: str
) -> str:
    return NatsChatMessage(
        senderId=messaging.sender.id,
        recipientId=messaging.recipient.id,
        timestamp=messaging.timestamp,
        text=messaging.message.text,
        mid=messaging.message.mid,
        appId=entry_id,
        attachments=[
            NatsChatMessageAttachment(
                type=attachment.type,
                payloadUrl=attachment.payload.url
            ) for attachment in messaging.message.attachments
        ],
        typeChat=chat_type
    ).json()


async def facebook_publish_to_nats_each_page_id(incoming_message: FacebookIncomingMessage):
    # create data in right format then publish into nats
    results = []
    for entry in incoming_message.entry:
        for messaging in entry.messaging:
            if messaging.message and messaging.recipient and messaging.recipient.id:
                nats_subject = constants.WEBHOOK_TO_CORECHAT_MESSAGE.format(
                    page_id=entry.id
                )
                if entry.id and nats_subject:
                    nats_msg = await facebook_create_nats_chat_message(entry.id, messaging, 'facebook')

                    _res = await stream_client_manager.publish_nats_all_clients(
                        nats_subject,
                        nats_msg.encode()
                    )
                    logger.info(f'publish to NATs-Facebook {nats_subject=} -> {nats_msg=} - {_res=}')
                    results.append({'subject': nats_subject, 'res': _res})
    return results

