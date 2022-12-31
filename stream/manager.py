# -*- coding: utf-8 -*-
import nats
from typing import Callable, List
from .base import BaseStreamClient
from .base import BaseStreamClientManager


class StreamClientManager(BaseStreamClientManager):
    '''
    Add a stream client
        client = StreamClient(NatsClient)
        await client.connect(settings.get_nats_serveres())

    '''

    async def get_all_nats_clients(self) -> List[BaseStreamClient]:
        print(self._clients)
        return [client for name, client in self._clients.items() if isinstance(client._client, nats.NATS)]

    async def publish_nats_all_clients(self,  *args, **kwargs):
        _result = {}
        for name, client in self._clients.items():
            if isinstance(client._client, nats.NATS):
                if client.is_connected:
                    res = await client.publish(*args, **kwargs)
                    _result.update({name: {'publish_res': res}})
        return _result

    async def subscribe_nats_all_clients(self, subject: str, handler: Callable, **kwargs):
        _result = {}
        for name, client in self._clients.items():
            if isinstance(client._client, nats.NATS):
                if client.is_connected:
                    res = await client.subscribe(subject, handler, **kwargs)
                    _result.update({name: {'result': res, 'subject': subject}})
        return _result

    async def publish_nats_dev_clients(self,  *args, **kwargs):
        _result = {}
        client = self._clients.get('NATs-Client-nats://172.24.222.112:4222')
        if client and client.is_connected:
            res = await client.publish(*args, **kwargs)
            _result.update({client.name: {'publish_res': res}})
        return _result

    async def subscribe_nats_dev_clients(self, subject: str, handler: Callable, **kwargs):
        _result = {}
        client = self._clients.get('NATs-Client-nats://172.24.222.112:4222')
        if client and client.is_connected:
            res = await client.subscribe(subject, handler, **kwargs)
            _result.update({client.name: {'result': res, 'subject': subject}})
        return _result
