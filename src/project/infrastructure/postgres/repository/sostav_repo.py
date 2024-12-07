from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, delete, insert, update

from src.project.schemas.sostav import SostavSchema, SostavCreateUpdateSchema
from src.project.infrastructure.postgres.new_models import Sostav

# from src.project.core.config import settings
from project.core.exceptions import intNotFound, UserAlreadyExists


class SostavRepository:
    _collection: Type[Sostav] = Sostav

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_sostav(
            self,
            session: AsyncSession,
    ) -> list[SostavSchema]:
        # query = f"select * from {settings.POSTGRES_SCHEMA}.sostav;"
        query = select(self._collection)
        sostav = await session.scalars(query)

        return [SostavSchema.model_validate(obj=sostav) for sostav in sostav.mappings().all()]

    async def get_sostav_by_id(
            self,
            session: AsyncSession,
            id: int,
    ) -> SostavSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == id)
        )
        user = await session.scalar(query)
        if not user:
            raise intNotFound(_object="id_sostav", _id=id)
        return SostavSchema.model_validate(obj=user)

    async def create_sostav(
            self,
            session: AsyncSession,
            sostav: SostavCreateUpdateSchema,
    ) -> SostavSchema:
        query = (
            insert(self._collection)
            .values(sostav.model_dump())
            .returning(self._collection)
        )

        created_user = await session.scalar(query)
        await session.flush()
        return SostavSchema.model_validate(obj=created_user)

    async def update_sostav(
            self,
            session: AsyncSession,
            id: int,
            user: SostavCreateUpdateSchema,
    ) -> SostavSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == id)
            .values(user.model_dump())
            .returning(self._collection)
        )
        updated_meal = await session.scalar(query)
        if not updated_meal:
            raise intNotFound(_object="id_sostav", _id=id)
        return SostavSchema.model_validate(obj=updated_meal)

    async def delete_sostav(
            self,
            session: AsyncSession,
            id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == id)
        result = await session.execute(query)
        if not result.rowcount:
            raise intNotFound(_object="id_sostav", _id=id)
