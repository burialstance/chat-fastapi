from typing import List

from tortoise.signals import post_save

from src.apps.users.models.user import User
from .models.search_options import SearchOptions


@post_save(User)
async def signal_create_default_search_options(
        sender: "Type[User]", instance: User, created: bool,
        using_db: "Optional[BaseDBAsyncClient]", update_fields: List[str]) -> None:

    if created:
        await SearchOptions.create(user=instance)
