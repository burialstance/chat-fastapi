from fastapi import HTTPException
from pydantic import UUID4

from src.conf.enums import MessengersEnum
from src.contrib.services.base_service import BaseService
from .models.messenger import Messenger
from . import schemas


class MessengerService(BaseService[Messenger]):

    async def get_messenger(self, **kwargs) -> Messenger:
        return await self._get(**kwargs)

    async def create_messenger(self, user_id: UUID4, form: schemas.MessengerCreate) -> Messenger:
        return await self._create(user_id=user_id, **form.dict(exclude_unset=True))

"""    async def _get_user_via_messenger(self, messenger_type: MessengersEnum, messenger_id: int):
        messenger = await self.get_messenger(
            messenger_type=messenger_type,
            messenger_id=messenger_id
        )
        if not messenger:
            raise HTTPException(404, 'messenger does not exists')

        await messenger.fetch_related('user')
        return messenger.user

    async def get_user_via_telegram(self, telegram_id: int):
        return await self._get_user_via_messenger(MessengersEnum.TELEGRAM, telegram_id)

    async def get_user_via_vkontakte(self, vkontakte_id: int):
        return await self._get_user_via_messenger(MessengersEnum.VKONTAKTE, vkontakte_id)"""


messenger_service = MessengerService(Messenger)
