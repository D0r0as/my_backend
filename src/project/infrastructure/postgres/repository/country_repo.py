from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.country import CountrySchema
from project.infrastructure.postgres.new_models import Country

from src.project.core.config import settings


class CountryRepository:
    _collection: Type[Country] = Country

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_country(
            self,
            session: AsyncSession,
    ) -> list[CountrySchema]:
        query = f"select * from {settings.POSTGRES_SCHEMA}.country;"

        country = await session.execute(text(query))

        return [CountrySchema.model_validate(obj=country) for country in country.mappings().all()]

