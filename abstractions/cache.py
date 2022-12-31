# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod


class AbsCacheClient(ABC):
    @property
    @abstractmethod
    async def name(self, *args, **kwargs) -> str:
        raise NotImplementedError

    @property
    @abstractmethod
    def is_connected(self, *args, **kwargs) -> bool:
        raise NotImplementedError

    @abstractmethod
    async def connect(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def disconnect(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def live_chat_get_client_info(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def live_chat_create_new_conversation(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def live_chat_save_message(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def live_chat_get_conversation_messages(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def live_chat_get_configs(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def live_chat_check_saleman_online_status(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def live_chat_set_uploaded_attachment_for_grid_msg(
        self,
        room_id: str, 
        grid_id: str, 
        attachment: str,
        job_id: str = None, 
        **kwargs
    ):
        raise NotImplementedError

    async def live_chat_get_uploaded_attachment_for_grid_msg(
        self,
        room_id: str, 
        grid_id: str, 
        **kwargs
    ):
        raise NotImplementedError

    async def live_chat_clear_uploaded_attachment_for_grid_msg(
        self,
        room_id: str, 
        grid_id: str, 
        **kwargs
    ):
        raise NotImplementedError

class AbsCacheClientManager(ABC):
    @abstractmethod
    async def add_client(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def remove_client(self, *args, **kwargs):
        raise NotImplementedError

    @abstractmethod
    async def disconnect_all(self, *args, **kwargs):
        raise NotImplementedError
