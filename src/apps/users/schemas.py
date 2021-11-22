from typing import Optional, List

from pydantic import BaseModel, UUID4

from src.apps.messengers.schemas import MessengerBase
from src.apps.users.models.user import User
from src.apps.profiles.schemas import ProfilePublic, ProfileBase

from tortoise.contrib.pydantic import pydantic_model_creator

User_Pydantic = pydantic_model_creator(User)


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]


class UserCreate(UserBase):
    ...


class UserPublic(UserBase):
    id: UUID4


class SignUpForm(BaseModel):
    user: UserCreate
    profile: Optional[ProfileBase]
    messenger: Optional[MessengerBase]
