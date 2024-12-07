from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, delete, update

from project.schemas.meals import MealsCreateUpdateSchema
from src.project.schemas.meals import MealsSchema
from src.project.infrastructure.postgres.models import Meals

#from src.project.core.config import settings
from project.core.exceptions import strNotFound, UserAlreadyExists

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
        #query = f"select * from {settings.POSTGRES_SCHEMA}.meals;"
        query = select(self._collection)
        meals = await session.scalars(query)

        return [MealsSchema.model_validate(obj=meals) for meals in meals.mappings().all()]

    async def get_meal_by_id(
            self,
            session: AsyncSession,
            id: str,
    ) -> MealsSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == id)
        )
        user = await session.scalar(query)
        if not user:
            raise strNotFound(_object="id_meal",_id=id)
        return MealsSchema.model_validate(obj=user)

    async def create_meal(
            self,
            session: AsyncSession,
            meal: MealsCreateUpdateSchema,
    ) -> MealsSchema:
        query = (
            insert(self._collection)
            .values(meal.model_dump())
            .returning(self._collection)
        )

        created_user = await session.scalar(query)
        await session.flush()
        return MealsSchema.model_validate(obj=created_user)

    async def update_meal(
            self,
            session: AsyncSession,
            id: str,
            user: MealsCreateUpdateSchema,
    ) -> MealsSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == id)
            .values(user.model_dump())
            .returning(self._collection)
        )
        updated_meal = await session.scalar(query)
        if not updated_meal:
            raise strNotFound(_object="id_meal",_id=id)
        return MealsSchema.model_validate(obj=updated_meal)

    async def delete_meal(
            self,
            session: AsyncSession,
            id: str
    ) -> None:
        query = delete(self._collection).where(self._collection.id == id)
        result = await session.execute(query)
        if not result.rowcount:
            raise strNotFound(_object="id_meal",_id=id)
