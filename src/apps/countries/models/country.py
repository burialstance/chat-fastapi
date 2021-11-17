from typing import Optional

from tortoise import fields, models


class Country(models.Model):
    name: str = fields.CharField(max_length=64)
    icon: Optional[str] = fields.CharField(max_length=8, null=True)
