from typing import Optional

from tortoise import fields, models, Tortoise

from src.utils.database import fetch_apps_models


class User(models.Model):
    id: int = fields.BigIntField(pk=True, index=True)
    first_name: Optional[str] = fields.CharField(max_length=64)
    last_name: Optional[str] = fields.CharField(max_length=64)

    profile: fields.OneToOneRelation['Profile']
    search_options: fields.OneToOneRelation['SearchOptions']


Tortoise.init_models(fetch_apps_models(), 'models')