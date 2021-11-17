from fastapi import APIRouter

from .. import schemas
from ..services.registration import signup_user
from src.apps.users.models.user import User

router = APIRouter()


@router.get('/', response_model=schemas.UserPublic)
async def get_user(id: int):
    return await User.get(id=id)


@router.post('/', response_model=schemas.UserPublic)
async def create_user(form: schemas.UserCreate):
    return await User.create(**form.dict(exclude_unset=True))


@router.post('/signup', response_model=schemas.UserPublic)
async def signup_new_user(form: schemas.SignUpForm):
    return await signup_user(form)
