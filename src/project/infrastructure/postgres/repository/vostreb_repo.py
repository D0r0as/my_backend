from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, delete, update, insert

from src.project.schemas.vostreb import VostrebSchema, VostrebCreateUpdateSchema
from src.project.infrastructure.postgres.new_models import Vostreb

# from src.project.core.config import settings
from project.core.exceptions import intNotFound, UserAlreadyExists


class VostrebRepository:
    _collection: Type[Vostreb] = Vostreb

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_vostreb(
            self,
            session: AsyncSession,
    ) -> list[VostrebSchema]:
        # query = f"select * from {settings.POSTGRES_SCHEMA}.vostreb;"
        query = select(self._collection)
        vostreb = await session.scalars(query)

        return [VostrebSchema.model_validate(obj=vostreb) for vostreb in vostreb.mappings().all()]

    async def get_vostreb_by_id(
            self,
            session: AsyncSession,
            id: int,
    ) -> VostrebSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == id)
        )
        user = await session.scalar(query)
        if not user:
            raise intNotFound(_object="id", _id=id)
        return VostrebSchema.model_validate(obj=user)

    async def create_vostreb(
            self,
            session: AsyncSession,
            vostreb: VostrebCreateUpdateSchema,
    ) -> VostrebSchema:
        query = (
            insert(self._collection)
            .values(vostreb.model_dump())
            .returning(self._collection)
        )

        created_user = await session.scalar(query)
        await session.flush()
        return VostrebSchema.model_validate(obj=created_user)

    async def update_vostreb(
            self,
            session: AsyncSession,
            id: int,
            user: VostrebCreateUpdateSchema,
    ) -> VostrebSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == id)
            .values(user.model_dump())
            .returning(self._collection)
        )
        updated_meal = await session.scalar(query)
        if not updated_meal:
            raise intNotFound(_object="id", _id=id)
        return VostrebSchema.model_validate(obj=updated_meal)

    async def delete_vostreb(
            self,
            session: AsyncSession,
            id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == id)
        result = await session.execute(query)
        if not result.rowcount:
            raise intNotFound(_object="id", _id=id)

