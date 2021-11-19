import logging
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from src.apps.countries.misc import populate_countries
from src.utils.database import fetch_apps_models
from src.apps.router import router
from src.conf.settings import settings
from src.exceptions.validate_request import ValidationErrorLoggingRoute
logging.basicConfig(level=logging.DEBUG if settings.DEBUG else logging.WARN)

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESC,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)
app.router.route_class = ValidationErrorLoggingRoute

app.add_middleware(
    CORSMiddleware,
    allow_origins='',
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(router)

register_tortoise(
    app=app,
    db_url=settings.DATABASE_URI,
    modules={'models': fetch_apps_models()},
    generate_schemas=True,
    add_exception_handlers=True
)


@app.on_event('startup')
async def on_startup():
    await populate_countries()
