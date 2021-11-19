from typing import Optional

from pydantic import BaseModel

from src.apps.users.models.user import User
from src.apps.profiles.schemas import ProfilePublic, ProfileBase
from src.apps.search_options.schemas import SearchOptionsPublic
from src.conf.enums import GendersEnum, CountriesEnum

from tortoise.contrib.pydantic import pydantic_model_creator

User_Pydantic = pydantic_model_creator(User)


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]


class UserCreate(UserBase):
    ...


class UserPublic(UserBase):
    id: int


class SignUpForm(BaseModel):
    user: UserCreate
    profile: Optional[ProfileBase]
