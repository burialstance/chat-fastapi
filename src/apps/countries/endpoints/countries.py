from typing import List
from fastapi import APIRouter

from .. import schemas
from ..services import country_service

router = APIRouter()


@router.post('/create', response_model=schemas.CountryPublic)
async def create_country(form: schemas.CountryCreate):
    return await country_service.create_country(form)


@router.get('/all', response_model=List[schemas.CountryPublic])
async def get_all_countries():
    return await country_service.get_all_countries()


@router.get('', response_model=schemas.CountryPublic)
async def get_country(id: int):
    return await country_service.get_country(id=id)