from fastapi import APIRouter

from .. import schemas
from ..services import profile_service

router = APIRouter()


@router.get('', response_model=schemas.ProfilePublic)
async def get_profile(user_id: int):
    return await profile_service.get_profile(user_id=user_id)


@router.put('/update', response_model=schemas.ProfilePublic)
async def update_profile(user_id: int, form: schemas.ProfileUpdate):
    return await profile_service.update_profile(user_id=user_id, form=form)