from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from src.apps.router import router
from src.conf.settings import settings
from src.utils.database import fetch_apps_models

app = FastAPI(
    title=settings.APP_TITLE,
    description=settings.APP_DESC,
    version=settings.APP_VERSION,
    debug=settings.DEBUG
)

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



