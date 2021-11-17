from typing import Optional

from tortoise import fields, models, Tortoise

from src.conf.enums import GendersEnum
from src.utils.database import fetch_apps_models


class SearchOptions(models.Model):
    user: fields.OneToOneRelation['User'] = fields.ForeignKeyField(
        'models.User', related_name='search_options', on_delete=fields.CASCADE, pk=True, index=True
    )

    from_age: Optional[int]
    to_age: Optional[int]
    gender: Optional[GendersEnum]
    country: fields.ForeignKeyNullableRelation['Country'] = fields.ForeignKeyField(
        'models.Country', related_name='search_options', on_delete=fields.SET_NULL, null=True
    )


Tortoise.init_models(fetch_apps_models(), 'models')
