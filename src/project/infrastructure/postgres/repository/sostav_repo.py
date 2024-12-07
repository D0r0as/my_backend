from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.project.schemas.sostav import SostavSchema
from src.project.infrastructure.postgres.new_models import Sostav

from src.project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.sostav;"

        sostav = await session.execute(text(query))

        return [SostavSchema.model_validate(obj=sostav) for sostav in sostav.mappings().all()]

