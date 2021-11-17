from typing import Optional

from tortoise import fields, models


class User(models.Model):
    id: int = fields.BigIntField(pk=True, index=True)
    first_name: Optional[str] = fields.CharField(max_length=64)
    last_name: Optional[str] = fields.CharField(max_length=64)
