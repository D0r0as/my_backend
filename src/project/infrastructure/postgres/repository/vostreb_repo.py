from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.project.schemas.vostreb import VostrebSchema
from src.project.infrastructure.postgres.new_models import Vostreb

from src.project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.vostreb;"

        vostreb = await session.execute(text(query))

        return [VostrebSchema.model_validate(obj=vostreb) for vostreb in vostreb.mappings().all()]

