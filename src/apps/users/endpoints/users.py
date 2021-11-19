from typing import List, Optional

from fastapi import APIRouter

from .. import schemas
from src.apps.users.models.user import User
from ..schemas import User_Pydantic
from ..services import user_service

router = APIRouter()


@router.get('/all', response_model=List[schemas.UserPublic])
async def get_all_users():
    return await user_service.get_all_users()


@router.get('/{id}', response_model=schemas.User_Pydantic)
async def get_user(id: int):
    user = await user_service.get_user(id=id)
    return await User_Pydantic.from_tortoise_orm(user)


@router.post('/signup', response_model=schemas.User_Pydantic)
async def signup_new_user(form: schemas.SignUpForm):
    user = await user_service.signup_new_user(form)
    return await User_Pydantic.from_tortoise_orm(user)
