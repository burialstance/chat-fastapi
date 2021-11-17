from typing import Optional

from pydantic import BaseModel

from src.conf.enums import GendersEnum, CountriesEnum


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    ...


class UserPublic(UserBase):
    id: int


class SignUpForm(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]

    age: Optional[int]
    country: Optional[CountriesEnum]
    gender: Optional[GendersEnum]
