from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, delete, update
from sqlalchemy.exc import IntegrityError

from src.project.schemas.users import UsersSchema, UsersCreateUpdateSchema
from src.project.infrastructure.postgres.new_models import Users

# from src.project.core.config import settings
from project.core.exceptions import strNotFound, UserAlreadyExists


class UsersRepository:
    _collection: Type[Users] = Users

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_users(
            self,
            session: AsyncSession,
    ) -> list[UsersSchema]:
        # query = f"select * from {settings.POSTGRES_SCHEMA}.users;"
        query = select(self._collection)

        users = await session.scalars(query)

        return [UsersSchema.model_validate(obj=users) for users in users.mappings().all()]

    async def get_user_by_id(
            self,
            session: AsyncSession,
            user_id: str,
    ) -> UsersSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == user_id)
        )
        user = await session.scalar(query)
        if not user:
            raise strNotFound(_object="id_username",_id=user_id)
        return UsersSchema.model_validate(obj=user)

    async def create_user(
            self,
            session: AsyncSession,
            user: UsersCreateUpdateSchema,
    ) -> UsersSchema:
        query = (
            insert(self._collection)
            .values(user.model_dump())
            .returning(self._collection)
        )
        try:
            created_user = await session.scalar(query)
            await session.flush()
        except IntegrityError:
            raise UserAlreadyExists(_id_username=user.id_username)
        return UsersSchema.model_validate(obj=created_user)

    async def update_user(
            self,
            session: AsyncSession,
            user_id: str,
            user: UsersCreateUpdateSchema,
    ) -> UsersSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == user_id)
            .values(user.model_dump())
            .returning(self._collection)
        )
        updated_user = await session.scalar(query)
        if not updated_user:
            raise strNotFound(_object="id_username",_id=user_id)
        return UsersSchema.model_validate(obj=updated_user)

    async def delete_user(
            self,
            session: AsyncSession,
            user_id: str
    ) -> None:
        query = delete(self._collection).where(self._collection.id == user_id)
        result = await session.execute(query)
        if not result.rowcount:
            raise strNotFound(_object="id_username",_id=user_id)
