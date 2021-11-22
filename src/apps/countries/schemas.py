from typing import Optional

from pydantic import BaseModel


class CountryBase(BaseModel):
    name: str
    icon: Optional[str]


class CountryPublic(CountryBase):
    id: int
