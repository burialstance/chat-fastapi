from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    ...


class UserPublic(UserBase):
    id: int
