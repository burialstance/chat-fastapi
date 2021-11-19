from src.contrib.services.base_service import BaseService
from .models.profile import Profile
from . import schemas


class ProfileService(BaseService[Profile]):

    async def get_profile(self, user_id: int) -> Profile:
        return await self._get(user_id=user_id)

    async def create_profile(self, form: schemas.ProfileCreate) -> Profile:
        return await self._create(**form.dict(exclude_unset=True))

    async def update_profile(self, user_id: int, form: schemas.ProfileUpdate) -> Profile:
        await self._update(pk=user_id, **form.dict(exclude_unset=True))
        return await self.get_profile(user_id=user_id)


profile_service = ProfileService(Profile)