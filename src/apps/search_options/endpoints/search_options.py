from fastapi import APIRouter

from .. import schemas
from ..services import search_options_service

router = APIRouter()


@router.get('', response_model=schemas.SearchOptionsPublic)
async def get_search_options(user_id: int):
    return await search_options_service.get_search_options(user_id=user_id)


@router.put('/update', response_model=schemas.SearchOptionsPublic)
async def update_search_options(user_id: int, form: schemas.SearchOptionsUpdate):
    return await search_options_service.update_search_options(user_id=user_id, form=form)