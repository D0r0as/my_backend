from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.project.schemas.meals import MealsSchema
from src.project.infrastructure.postgres.models import Meals

from src.project.core.config import settings


class MealsRepository:
    _collection: Type[Meals] = Meals

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_meals(
            self,
            session: AsyncSession,
    ) -> list[MealsSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.meals;"

        meals = await session.execute(text(query))

        return [MealsSchema.model_validate(obj=meals) for meals in meals.mappings().all()]

