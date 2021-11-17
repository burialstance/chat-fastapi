from fastapi import APIRouter

from .. import schemas
from ..models.search_options import SearchOptions

router = APIRouter()


@router.get('/{user_id}', response_model=schemas.SearchOptionsPublic)
async def get_search_options(user_id: int):
    return await SearchOptions.get(user_id=user_id)