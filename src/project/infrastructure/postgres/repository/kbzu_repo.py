from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, delete, insert, update

from project.schemas.kbzu import KbzuSchema, KbzuCreateUpdateSchema
from project.infrastructure.postgres.new_models import Kbzu

#from src.project.core.config import settings
from project.core.exceptions import intNotFound, UserAlreadyExists


class KbzuRepository:
    _collection: Type[Kbzu] = Kbzu

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_kbzu(
            self,
            session: AsyncSession,
    ) -> list[KbzuSchema]:
        #query = f"select * from {settings.POSTGRES_SCHEMA}.kbzu;"
        query = select(self._collection)
        kbzu = await session.scalars(query)

        return [KbzuSchema.model_validate(obj=kbzu) for kbzu in kbzu.mappings().all()]

    async def get_kbzu_by_id(
            self,
            session: AsyncSession,
            id: int,
    ) -> KbzuSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == id)
        )
        user = await session.scalar(query)
        if not user:
            raise intNotFound(_object="id_kbzu",_id=id)
        return KbzuSchema.model_validate(obj=user)

    async def create_kbzu(
            self,
            session: AsyncSession,
            user: KbzuCreateUpdateSchema,
    ) -> KbzuSchema:
        query = (
            insert(self._collection)
            .values(user.model_dump())
            .returning(self._collection)
        )
        created_user = await session.scalar(query)
        await session.flush()

        return KbzuSchema.model_validate(obj=created_user)

    async def update_kbzu(
            self,
            session: AsyncSession,
            id: int,
            user: KbzuCreateUpdateSchema,
    ) -> KbzuSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == id)
            .values(user.model_dump())
            .returning(self._collection)
        )
        updated_user = await session.scalar(query)
        if not updated_user:
            raise intNotFound(_object="id_kbzu",_id=id)
        return KbzuSchema.model_validate(obj=updated_user)

    async def delete_kbzu(
            self,
            session: AsyncSession,
            id: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == id)
        result = await session.execute(query)
        if not result.rowcount:
            raise intNotFound(_object="id_kbzu",_id=id)
