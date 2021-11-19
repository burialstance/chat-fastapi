from fastapi import APIRouter

from .. import schemas
from ..services.registration import signup_user
from src.apps.users.models.user import User

router = APIRouter()


@router.get('/{id}', response_model=schemas.UserPublic)
async def get_user(id: int):
    return await User.get(id=id)


@router.post('/signup', response_model=schemas.UserPublic)
async def signup_new_user(form: schemas.SignUpForm):
    return await signup_user(form)
