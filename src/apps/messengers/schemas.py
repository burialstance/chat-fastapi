from pydantic import BaseModel, UUID4

from src.conf.enums import MessengersEnum


class MessengerBase(BaseModel):
    messenger_type: MessengersEnum
    messenger_id: int


class MessengerPublic(MessengerBase):
    user_id: UUID4


class MessengerCreate(MessengerBase):
    user_id: UUID4


class MessengerUpdate(MessengerBase):
    user_id: UUID4
