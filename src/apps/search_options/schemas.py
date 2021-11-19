from typing import Optional

from pydantic import BaseModel

from src.apps.countries.schemas import CountryPublic
from src.conf.enums import GendersEnum


class SearchOptionsBase(BaseModel):
    from_age: Optional[int]
    to_age: Optional[int]
    gender: Optional[GendersEnum]
    country: Optional[CountryPublic]


class SearchOptionsCreate(SearchOptionsBase):
    user_id: int


class SearchOptionsPublic(SearchOptionsBase):
    ...


class SearchOptionsUpdate(SearchOptionsBase):
    ...
