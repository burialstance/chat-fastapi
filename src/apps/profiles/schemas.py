from typing import Optional
from pydantic import BaseModel

from src.conf.enums import GendersEnum
from ..countries.schemas import CountryPublic

class ProfileBase(BaseModel):
    age: Optional[int]
    gender: Optional[GendersEnum]
    country: Optional[CountryPublic]


class ProfileCreate(ProfileBase):
    user_id: int


class ProfilePublic(ProfileBase):
    ...


class ProfileUpdate(ProfileBase):
    ...
