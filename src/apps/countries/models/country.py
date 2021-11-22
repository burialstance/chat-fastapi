from typing import Optional

from tortoise import fields, models
from src.conf.enums import CountriesEnum


class Country(models.Model):
    name: CountriesEnum = fields.CharEnumField(CountriesEnum, unique=True)
    icon: Optional[str] = fields.CharField(max_length=8, null=True)

    class PydanticMeta:
        exclude = (
            'profiles', 'search_options'
        )
