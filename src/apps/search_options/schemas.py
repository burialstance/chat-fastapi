from typing import Optional

from pydantic import BaseModel

from src.conf.enums import GendersEnum


class SearchOptionsBase(BaseModel):
    from_age: Optional[int]
    to_age: Optional[int]
    gender: Optional[GendersEnum]
    country_id: Optional[int]


class SearchOptionsCreate(SearchOptionsBase):
    user_id: int


class SearchOptionsPublic(SearchOptionsBase):
    user_id: int


class SearchOptionsUpdate(SearchOptionsBase):
    ...
