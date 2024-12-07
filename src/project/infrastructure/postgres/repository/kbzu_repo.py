from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.kbzu import KbzuSchema
from project.infrastructure.postgres.new_models import Kbzu

from src.project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.kbzu;"

        kbzu = await session.execute(text(query))

        return [KbzuSchema.model_validate(obj=kbzu) for kbzu in kbzu.mappings().all()]

