from fastapi import APIRouter

from .. import schemas
from ..models.profile import Profile


router = APIRouter()


@router.get('/{id}', response_model=schemas.ProfilePublic)
async def get_profile(user_id: int):
    return await Profile.get(user_id=user_id)


