from typing import TypeVar, Type, Generic, Optional, List, Any

from tortoise import models
from fastapi.exceptions import HTTPException

ModelType = TypeVar("ModelType", bound=models.Model)

NOT_FOUND_EXCEPTION = HTTPException(404, 'object does not exists')
ALREADY_EXISTS_EXCEPTIONS = HTTPException(422, 'already exists')


class BaseService(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def _get(self, **kwargs) -> ModelType:
        return await self.model.filter(**kwargs).first()

    async def _create(self, **kwargs) -> ModelType:
        return await self.model.create(**kwargs)

    async def _update(self, pk: Any, **kwargs):
        lookup = {self.model._meta.pk_attr: pk}
        return await self.model.filter(**lookup).update(**kwargs)

    async def _delete(self, **kwargs) -> ModelType:
        instance = await self.model.filter(**kwargs).first()
        if not instance:
            raise NOT_FOUND_EXCEPTION
        await instance.delete()
        return instance

    async def _all(self) -> List[Optional[ModelType]]:
        return await self.model.all()

    async def _exists(self, **kwargs) -> bool:
        return await self.model.exists(**kwargs)
