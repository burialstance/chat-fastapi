from typing import Optional

from tortoise import fields, models, Tortoise
from pydantic import UUID4
from src.utils.database import fetch_apps_models


class User(models.Model):
    id: UUID4 = fields.UUIDField(pk=True, index=True)

    first_name: Optional[str] = fields.CharField(max_length=64, null=True)
    last_name: Optional[str] = fields.CharField(max_length=64, null=True)

    is_active: bool = fields.BooleanField(default=True)


Tortoise.init_models(fetch_apps_models(), 'models')