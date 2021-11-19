from typing import Optional

from tortoise import fields, models, Tortoise

from src.conf.enums import GendersEnum
from src.utils.database import fetch_apps_models


class SearchOptions(models.Model):
    user: fields.OneToOneRelation['User'] = fields.OneToOneField(
        'models.User', related_name='search_options', on_delete=fields.CASCADE
    )

    from_age: Optional[int] = fields.IntField(null=True)
    to_age: Optional[int] = fields.IntField(null=True)
    gender: Optional[GendersEnum] = fields.CharEnumField(GendersEnum, null=True)
    country: fields.ForeignKeyNullableRelation['Country'] = fields.ForeignKeyField(
        'models.Country', related_name='search_options', on_delete=fields.SET_NULL, null=True
    )

    class PydanticMeta:
        exclude = ('id',)


Tortoise.init_models(fetch_apps_models(), 'models')
