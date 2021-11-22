from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import UUID4

from .. import schemas
from ..services import profile_service

router = APIRouter()


@router.get('/{user_id}', response_model=schemas.ProfilePublic)
async def get_profile(user_id: UUID4):
    return await profile_service.get_profile(user_id=user_id)


@router.put('/{user_id}/update', response_model=schemas.ProfilePublic)
async def update_profile(user_id: UUID4, form: schemas.ProfileUpdate):
    return await profile_service.update_profile(user_id=user_id, form=form)