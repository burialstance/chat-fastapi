from typing import Optional
from tortoise import fields, models, Tortoise

from src.utils.database import fetch_apps_models
from src.conf.enums import GendersEnum


class Profile(models.Model):
    user: fields.OneToOneRelation['User'] = fields.OneToOneField(
        'models.User', related_name='profile', on_delete=fields.CASCADE, pk=True, index=True
    )

    age: Optional[int] = fields.SmallIntField(null=True)
    gender: Optional[GendersEnum] = fields.CharEnumField(GendersEnum, null=True)
    country: fields.ForeignKeyNullableRelation['Country'] = fields.ForeignKeyField(
        'models.Country', related_name='profiles', on_delete=fields.SET_NULL, null=True
    )

    class PydanticMeta:
        exclude = ('id',)


Tortoise.init_models(fetch_apps_models(), 'models')
