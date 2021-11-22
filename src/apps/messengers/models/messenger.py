from tortoise import models, fields, Tortoise

from src.utils.database import fetch_apps_models
from src.conf.enums import MessengersEnum


class Messenger(models.Model):
    user: fields.ForeignKeyRelation['User'] = fields.ForeignKeyField(
        'models.User', related_name='messengers', on_delete=fields.CASCADE
    )

    messenger_type: MessengersEnum = fields.CharEnumField(MessengersEnum)
    messenger_id: int = fields.BigIntField()

    class Meta:
        unique_together = (
            ('messenger_type', 'messenger_id')
        )


Tortoise.init_models(fetch_apps_models(), 'models')
