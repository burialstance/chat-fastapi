from typing import Optional

from tortoise import fields, models, Tortoise

from src.utils.database import fetch_apps_models


class User(models.Model):
    id: int = fields.BigIntField(pk=True, index=True)

    first_name: Optional[str] = fields.CharField(max_length=64, null=True)
    last_name: Optional[str] = fields.CharField(max_length=64, null=True)


Tortoise.init_models(fetch_apps_models(), 'models')