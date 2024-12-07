from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from src.project.schemas.users import UsersSchema
from src.project.infrastructure.postgres.new_models import Users

from src.project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.users;"

        users = await session.execute(text(query))

        return [UsersSchema.model_validate(obj=users) for users in users.mappings().all()]

