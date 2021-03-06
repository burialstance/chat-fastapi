from fastapi import APIRouter

from src.apps.users.endpoints import users
from src.apps.countries.endpoints import countries
from src.apps.profiles.endpoints import profiles
from src.apps.search_options.endpoints import search_options
from src.apps.messengers.endpoints import messengers

router = APIRouter(prefix='/api')

router.include_router(users.router, prefix='/users', tags=['users'])
router.include_router(profiles.router, prefix='/profiles', tags=['profiles'])
router.include_router(countries.router, prefix='/countries', tags=['countries'])
router.include_router(search_options.router, prefix='/search_options', tags=['search_options'])
router.include_router(messengers.router, prefix='/messengers', tags=['messengers'])

