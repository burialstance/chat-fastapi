from fastapi import APIRouter
from src.apps.users.schemas import UserPublic, UserCreate

from src.apps.users.models.user import User

router = APIRouter()


@router.get('/', response_model=UserPublic)
async def get_user(id: int):
    user = await User.get(id=id)
    return UserPublic.from_orm(user)


@router.post('/', response_model=UserPublic)
async def create_user(form: UserCreate):
    user = await User.create(**form.dict(exclude_unset=True))
    return UserPublic.from_orm(user)