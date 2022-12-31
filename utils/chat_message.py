# -*- coding: utf-8 -*-
import logging
from nats import utils
import constants
from schemas.chat_message_schema import FacebookIncomingMessage


debug_logger = logging.getLogger(constants.DEBUG_LOGGER_NAME)


async def handle_incoming_chat_message(request_body: bytes):
    try:
        incoming_message = FacebookIncomingMessage.parse_raw(request_body)
    except Exception as e:
        debug_logger.exception(f'facebook parse FacebookIncomingMessage get exception {e}')
        return

    res = await utils.facebook_publish_to_nats_each_page_id(incoming_message)
    debug_logger.info(f'facebook publish nats results {res=}')
