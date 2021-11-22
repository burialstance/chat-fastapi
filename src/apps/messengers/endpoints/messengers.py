from fastapi import APIRouter

from src.conf.enums import MessengersEnum
from .. import schemas
from ..services import messenger_service
from ..schemas import MessengerPublic

router = APIRouter()


@router.post('/create', response_model=schemas.MessengerPublic)
async def create_messenger(form: schemas.MessengerCreate):
    return await messenger_service.create_messenger(form=form)


@router.get('/{messenger_type}/{messenger_id}', response_model=MessengerPublic)
async def get_messenger_vkontakte(messenger_type: MessengersEnum, messenger_id: int):
    return await messenger_service.get_messenger(
        messenger_type=messenger_type,
        messenger_id=messenger_id
    )
