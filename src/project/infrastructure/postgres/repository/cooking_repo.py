from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete

from project.schemas.cooking import CookingSchema
from project.infrastructure.postgres.new_models import Cooking

from src.project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.cooking;"

        cooking = await session.execute(text(query))

        return [CookingSchema.model_validate(obj=cooking) for cooking in cooking.mappings().all()]

