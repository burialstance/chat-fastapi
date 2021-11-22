from typing import Optional, List

from src.contrib.services.base_service import BaseService
from .models.country import Country
from . import schemas


class CountryService(BaseService[Country]):

    async def get_country(self, id: int) -> Country:
        return await self._get(id=id)

    async def get_all_countries(self) -> List[Optional[Country]]:
        return await self._all()


country_service = CountryService(Country)
