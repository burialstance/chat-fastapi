from typing import List, Optional

from fastapi import APIRouter
from pydantic import UUID4

from src.conf.enums import MessengersEnum
from .. import schemas
from ..schemas import User_Pydantic
from ..services import user_service

router = APIRouter()


@router.get('/all', response_model=List[schemas.UserPublic])
async def get_all_users():
    return await user_service.get_all_users()


@router.get('/{uuid}', response_model=schemas.User_Pydantic)
async def get_user(uuid: UUID4):
    user = await user_service.get_user(uuid=uuid)
    return await User_Pydantic.from_tortoise_orm(user)


@router.post('/signup', response_model=schemas.User_Pydantic)
async def signup_new_user(form: schemas.SignUpForm):
    user = await user_service.signup_new_user(form)
    return await User_Pydantic.from_tortoise_orm(user)
