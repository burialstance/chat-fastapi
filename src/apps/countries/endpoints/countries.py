from typing import List
from fastapi import APIRouter

from .. import schemas
from ..models.country import Country

router = APIRouter()


@router.get('/', response_model=List[schemas.CountryPublic])
async def get_all_countries():
    return await Country.all()


@router.get('/{id}', response_model=schemas.CountryPublic)
async def get_country(id: int):
    return await Country.get(id=id)