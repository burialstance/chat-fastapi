from typing import Optional

from tortoise import fields, models


class Country(models.Model):
    name: str = fields.CharField(max_length=64, unique=True)
    icon: Optional[str] = fields.CharField(max_length=8, null=True)

    class PydanticMeta:
        exclude = (
            'profiles', 'search_options'
        )
