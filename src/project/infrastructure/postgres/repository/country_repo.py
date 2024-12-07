from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, update, delete, insert

from project.schemas.country import CountrySchema, CountryCreateUpdateSchema
from project.infrastructure.postgres.new_models import Country

#from src.project.core.config import settings
from project.core.exceptions import intNotFound

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
        #query = f"select * from {settings.POSTGRES_SCHEMA}.country;"
        query = select(self._collection)
        country = await session.scalars(query)

        return [CountrySchema.model_validate(obj=country) for country in country.all()]

    async def get_country_id(
            self,
            session: AsyncSession,
            id_country: int,
    ) -> CountrySchema:
        query = (
            select(self._collection)
            .where(self._collection.id == id_country)
        )
        country = await session.scalar(query)
        if not country:
            raise intNotFound(_object="id",_id=id_country)
        return CountrySchema.model_validate(obj=country)

    async def create_country(
            self,
            session: AsyncSession,
            country: CountryCreateUpdateSchema,
    ) -> CountrySchema:
        query = (
            insert(self._collection)
            .values(country.model_dump())
            .returning(self._collection)
        )
        created_country = await session.scalar(query)
        await session.flush()

        return CountrySchema.model_validate(obj=created_country)

    async def update_country(
            self,
            session: AsyncSession,
            id_country: int,
            country: CountryCreateUpdateSchema,
    ) -> CountrySchema:
        query = (
            update(self._collection)
            .where(self._collection.id == id_country)
            .values(country.model_dump())
            .returning(self._collection)
        )
        updated_user = await session.scalar(query)
        if not updated_user:
            raise intNotFound(_object="id",_id=id_country)
        return CountrySchema.model_validate(obj=updated_user)

    async def delete_country(
            self,
            session: AsyncSession,
            id_country: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == id_country)
        result = await session.execute(query)
        if not result.rowcount:
            raise intNotFound(_object="id",_id=id_country)