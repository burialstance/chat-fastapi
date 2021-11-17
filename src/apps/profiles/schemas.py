from typing import Optional
from pydantic import BaseModel

from src.conf.enums import GendersEnum


class ProfileBase(BaseModel):
    user_id: int
    age: Optional[int]
    gender: Optional[GendersEnum]
    country_id: Optional[int]


class ProfileCreate(ProfileBase):
    ...


class ProfilePublic(ProfileBase):
    ...
