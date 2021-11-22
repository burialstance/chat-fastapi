from typing import Optional
from pydantic import BaseModel, UUID4
from src.conf.enums import GendersEnum
from ..countries.schemas import CountryPublic


class ProfileBase(BaseModel):
    age: Optional[int]
    gender: Optional[GendersEnum]
    country_id: Optional[int]


class ProfilePublic(ProfileBase):
    user_id: UUID4


class ProfileUpdate(ProfileBase):
    ...
