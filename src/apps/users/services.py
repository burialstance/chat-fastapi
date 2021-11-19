from typing import Optional, List

from src.contrib.services.base_service import BaseService
from src.apps.profiles.services import profile_service

from .models.user import User
from . import schemas

"""
from src.apps.users.models.user import User
from src.apps.profiles.models.profile import Profile
from src.apps.countries.models.country import Country
from src.apps.search_options.models.search_options import SearchOptions

from .. import schemas


async def signup_user(form: schemas.SignUpForm) -> schemas.UserPublic:
    user = await User.create(
        first_name=form.first_name,
        last_name=form.last_name
    )

    country = await Country.get(name=form.country.value)
    profile = await Profile.create(
        user=user,
        age=form.age,
        gender=form.gender,
        country=country
    )
    search_options = await SearchOptions.create(user=user)

    return schemas.UserPublic.from_orm(user)
"""


class UserService(BaseService[User]):

    async def get_user(self, id: int) -> User:
        return await self._get(id=id)

    async def create_user(self, form: schemas.UserCreate):
        return await self._create(**form.dict(exclude_unset=True))

    async def get_all_users(self) -> List[Optional[User]]:
        return await self._all()

    async def signup_new_user(self, form: schemas.SignUpForm) -> User:
        user = await self.create_user(form=form.user)

        if form.profile:
            await profile_service.update_profile(user_id=user.id, form=form.profile)

        return user


user_service = UserService(User)
