from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete
from sqlalchemy.exc import IntegrityError

from project.schemas.cooking import CookingCreateUpdateSchema, CookingSchema
from project.infrastructure.postgres.new_models import Cooking

#from src.project.core.config import settings
from project.core.exceptions import strNotFound

class CookingRepository:
    _collection: Type[Cooking] = Cooking

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_cooking(
            self,
            session: AsyncSession,
    ) -> list[CookingSchema]:
        #query = f"select * from {settings.POSTGRES_SCHEMA}.cooking;"
        query = select(self._collection)
        cooking = await session.scalars(query)

        return [CookingSchema.model_validate(obj=cooking) for cooking in cooking.all()]

    async def get_cooking_by_id(
            self,
            session: AsyncSession,
            id_sposob: str,
    ) -> CookingSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == id_sposob)
        )
        cooking = await session.scalar(query)
        if not cooking:
            raise strNotFound(_object="sposob",_id=id_sposob)
        return CookingSchema.model_validate(obj=cooking)

    async def create_sposob(
            self,
            session: AsyncSession,
            sposob1: CookingCreateUpdateSchema,
    ) -> CookingSchema:
        query = (
            insert(self._collection)
            .values(sposob1.model_dump())
            .returning(self._collection)
        )
        created_sposob = await session.scalar(query)
        await session.flush()

        return CookingSchema.model_validate(obj=created_sposob)

    async def update_sposob(
            self,
            session: AsyncSession,
            id_sposob: str,
            sposob: CookingCreateUpdateSchema,
    ) -> CookingSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == id_sposob)
            .values(sposob.model_dump())
            .returning(self._collection)
        )
        updated_sposob = await session.scalar(query)
        if not updated_sposob:
            raise strNotFound(_object="sposob", _id=id_sposob)
        return CookingSchema.model_validate(obj=updated_sposob)

    async def delete_sposob(
            self,
            session: AsyncSession,
            id_sposob: str
    ) -> None:
        query = delete(self._collection).where(self._collection.id == id_sposob)
        result = await session.execute(query)
        if not result.rowcount:
            raise strNotFound(_object="sposob",_id=id_sposob)