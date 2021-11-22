from typing import Optional

from pydantic import BaseModel, UUID4

from src.apps.countries.schemas import CountryPublic
from src.conf.enums import GendersEnum


class SearchOptionsBase(BaseModel):
    from_age: Optional[int]
    to_age: Optional[int]
    gender: Optional[GendersEnum]
    country_id: Optional[int]


class SearchOptionsPublic(SearchOptionsBase):
    user_id: UUID4


class SearchOptionsUpdate(SearchOptionsBase):
    ...
