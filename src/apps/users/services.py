from typing import Optional, List

from fastapi import HTTPException
from pydantic import UUID4

from src.contrib.services.base_service import BaseService
from src.apps.profiles.services import profile_service

from .models.user import User
from . import schemas
from ..messengers.services import messenger_service


class UserService(BaseService[User]):

    async def get_user(self, uuid: UUID4) -> User:
        return await self._get(id=uuid)

    async def create_user(self, form: schemas.UserCreate):
        return await self._create(**form.dict(exclude_unset=True))

    async def get_all_users(self) -> List[Optional[User]]:
        return await self._all()

    async def signup_new_user(self, form: schemas.SignUpForm) -> User:
        user = await self.create_user(form=form.user)

        if form.profile:
            await profile_service.update_profile(user_id=user.id, form=form.profile)

        if form.messenger:
            await messenger_service.create_messenger(user_id=user.id, form=form.messenger)

        return user




user_service = UserService(User)
