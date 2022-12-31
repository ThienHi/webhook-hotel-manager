# -*- coding: utf-8 -*-
import logging
from fastapi import APIRouter, Request, HTTPException, Response
import constants
from utils.chat_message import handle_incoming_chat_message
from fastapi import FastAPI

app = FastAPI()


# router = APIRouter(prefix='/chat_message')
logger = logging.getLogger(constants.FACEBOOK_WEBHOOK_LOGGER_NAME)
debug_logger = logging.getLogger(constants.DEBUG_LOGGER_NAME)


@app.post('/receiver')
async def on_incoming_message(
    request: Request
    # incoming_message: IncomingMessage
):
    body = await request.body()
    debug_logger.info(f'facebook get request {body=}')
    # print(f'request body {body}')

    await handle_incoming_chat_message(body)
    return Response(status_code=200, content='EVENT RECEIVED')


@app.get('/receiver')
async def on_verify(request: Request):
    hub_mode = request.query_params.get('hub.mode')
    hub_challenge = request.query_params.get('hub.challenge')
    hub_verify_token = request.query_params.get('hub.verify_token')
    print(f'hub_mode {hub_mode} - hub_challenge {hub_challenge} - hub_verify_token {hub_verify_token}')
    if hub_mode == constants.FB_WEBHOOK_SUBSCRIBE and hub_verify_token == constants.FB_WEBHOOK_VERIFICATION_TOKEN:
        return Response(status_code=200, content=hub_challenge)
    else:
        raise HTTPException(status_code=403, detail='Forbidden reason token error')
