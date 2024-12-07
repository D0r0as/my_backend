from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.ingredients import IngredientsSchema
from project.infrastructure.postgres.new_models import Ingredients

from src.project.core.config import settings


class IngredientsRepository:
    _collection: Type[Ingredients] = Ingredients

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_ingredients(
            self,
            session: AsyncSession,
    ) -> list[IngredientsSchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.ingredients;"

        ingredients = await session.execute(text(query))

        return [IngredientsSchema.model_validate(obj=ingredients) for ingredients in ingredients.mappings().all()]

