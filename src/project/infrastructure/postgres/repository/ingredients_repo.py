from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, delete, update

from project.schemas.ingredients import IngredientsSchema, IngredientsCreateUpdateSchema
from project.infrastructure.postgres.new_models import Ingredients

#from src.project.core.config import settings
from project.core.exceptions import strNotFound, UserAlreadyExists


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
        #query = f"select * from {settings.POSTGRES_SCHEMA}.ingredients;"
        query = select(self._collection)
        ingredients = await session.scalars(query)

        return [IngredientsSchema.model_validate(obj=ingredients) for ingredients in ingredients.mappings().all()]

    async def get_ing_by_id(
            self,
            session: AsyncSession,
            id: str,
    ) -> IngredientsSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == id)
        )
        ing = await session.scalar(query)
        if not ing:
            raise strNotFound(_object="id_ingredient",_id=id)
        return IngredientsSchema.model_validate(obj=ing)

    async def create_ing(
            self,
            session: AsyncSession,
            ing: IngredientsCreateUpdateSchema,
    ) -> IngredientsSchema:
        query = (
            insert(self._collection)
            .values(ing.model_dump())
            .returning(self._collection)
        )
        created_ing = await session.scalar(query)
        await session.flush()
        return IngredientsSchema.model_validate(obj=created_ing)

    async def update_ing(
            self,
            session: AsyncSession,
            id: str,
            user: IngredientsCreateUpdateSchema,
    ) -> IngredientsSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == id)
            .values(user.model_dump())
            .returning(self._collection)
        )
        updated_user = await session.scalar(query)
        if not updated_user:
            raise strNotFound(_object="id_ingredient",_id=id)
        return IngredientsSchema.model_validate(obj=updated_user)

    async def delete_ing(
            self,
            session: AsyncSession,
            id: str
    ) -> None:
        query = delete(self._collection).where(self._collection.id == user_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise strNotFound(_object="id_ingredient",_id=id)