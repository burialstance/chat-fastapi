from typing import Optional
from pydantic import BaseModel

from src.conf.enums import GendersEnum


class ProfileBase(BaseModel):
    age: Optional[int]
    gender: Optional[GendersEnum]
    country_id: Optional[int]


class ProfileCreate(ProfileBase):
    user_id: int


class ProfilePublic(ProfileBase):
    user_id: int


class ProfileUpdate(ProfileBase):
    ...
