from fastapi import APIRouter
from pydantic import UUID4

from .. import schemas
from ..services import search_options_service

router = APIRouter()


@router.get('/{user_id}', response_model=schemas.SearchOptionsPublic)
async def get_search_options(user_id: UUID4):
    return await search_options_service.get_search_options(user_id=user_id)


@router.put('/{user_id}/update', response_model=schemas.SearchOptionsPublic)
async def update_search_options(user_id: UUID4, form: schemas.SearchOptionsUpdate):
    return await search_options_service.update_search_options(user_id=user_id, form=form)
