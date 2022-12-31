# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class AbsNotificationClient(ABC):
    @abstractmethod
    async def connect(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def disconnect(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def notify(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def notify_error(self, *args, **kwargs):
        raise NotImplementedError


class AbsNotificationManager(ABC):
    @abstractmethod
    async def setup(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def notify(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def notify_error(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def add_client(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def remove_client(self, *args, **kwargs):
        raise NotImplementedError
