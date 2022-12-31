# -*- coding: utf-8 -*-


# -------------------------------------------------------------------
# Webhook <-----------> CoreChat
WEBHOOK_TO_CORECHAT_MESSAGE = 'Webhook.To.CoreChat.Message.{page_id}'       # messsage send from webhook to core chat
# messsage send from CORECHAT to WEBHOOK LIVECHAT ANONYMOUS
CORECHAT_TO_WEBHOOK_LIVECHAT = "CoreChat.To.Webhook.LiveChat.{page_id}"
# --------End--------------------------------------------------------


# -------------------------------------------------------------------
# ChatWs <-----------> CoreChat
CORECHAT_TO_WEBSOCKET_FACEBOOK = "CoreChat.To.ChatWs.FaceBook.{page_id}"   # CORECHAT OF OMNICHAT SERVICE -> WS FACEBOOK
CORECHAT_TO_WEBSOCKET_LIVECHAT = "CoreChat.To.ChatWs.LiveChat.{page_id}"   # CORECHAT OF OMNICHAT SERVICE -> WS LIVECHAT
CORECHAT_TO_WEBSOCKET_ZALO = "CoreChat.To.ChatWs.Zalo.{page_id}"   # CORECHAT OF OMNICHAT SERVICE -> WS ZALO
# --------End--------------------------------------------------------


# message type
NATS_MSG_TYPE_TEXT = "text"
NATS_MSG_TYPE_FOLLOW = "follow"
NATS_MSG_TYPE_UNFOLLOW = "unfollow"
NATS_MSG_TYPE_LEAVE_LIVECHAT_LOG = "leave-livechat-log"


# -------------------------------------------------------------------
# ChatWs <-----------> Webhook
CHATWS_TO_WEBHOOK_LIVECHAT = "ChatWs.To.Webhook.LiveChat.{page_id}"   # CORECHAT OF OMNICHAT SERVICE -> WS FACEBOOK
# --------End--------------------------------------------------------
