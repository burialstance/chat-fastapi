from apps.messengers.models.messenger import Messenger
from apps.messengers.services import messenger_service
from conf.enums import MessengersEnum


async def get_messenger(messenger_type: MessengersEnum, id: int) -> Messenger:
    return await messenger_service.get_messenger(
        messenger_type=messenger_type, messenger_id=id
    )
