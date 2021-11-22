from pydantic import UUID4

from src.contrib.services.base_service import BaseService
from .models.search_options import SearchOptions
from . import schemas


class SearchOptionsService(BaseService[SearchOptions]):

    async def get_search_options(self, user_id: UUID4) -> SearchOptions:
        return await self._get(user_id=user_id)

    async def update_search_options(self, user_id: UUID4, form: schemas.SearchOptionsUpdate) -> SearchOptions:
        await self._update(pk=user_id, **form.dict(exclude_unset=True))
        return await self.get_search_options(user_id=user_id)


search_options_service = SearchOptionsService(SearchOptions)
