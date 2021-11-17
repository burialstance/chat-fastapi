from typing import Optional

from pydantic import BaseModel

from src.conf.enums import GendersEnum



class SearchOptionsBase(BaseModel):
    user_id: int
    from_age: Optional[int]
    to_age: Optional[int]
    gender: Optional[GendersEnum]
    country_id: Optional[int]


class SearchOptionsPublic(SearchOptionsBase):
    ...


class SearchOptionsCreate(SearchOptionsBase):
    ...
