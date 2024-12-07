from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text, select, insert, update, delete

from project.schemas.feedback import FeedbackSchema, FeedbackCreateUpdateSchema
from project.infrastructure.postgres.new_models import Feedback

#from src.project.core.config import settings
from project.core.exceptions import intNotFound, UserAlreadyExists


class FeedbackRepository:
    _collection: Type[Feedback] = Feedback

    async def check_connection(
            self,
            session: AsyncSession,
    ) -> bool:
        query = "select 1;"

        result = await session.scalar(text(query))

        return True if result else False

    async def get_all_feedback(
            self,
            session: AsyncSession,
    ) -> list[FeedbackSchema]:
        #query = f"select * from {settings.POSTGRES_SCHEMA}.feedback;"
        query = select(self._collection)
        feedback = await session.scalars(query)

        return [FeedbackSchema.model_validate(obj=feedback) for feedback in feedback.all()]

    async def get_feedback_by_id(
            self,
            session: AsyncSession,
            id_coment: int,
    ) -> FeedbackSchema:
        query = (
            select(self._collection)
            .where(self._collection.id == id_coment)
        )
        user = await session.scalar(query)
        if not user:
            raise intNotFound(_object="id_coment",_id=id_coment)
        return FeedbackSchema.model_validate(obj=user)

    async def create_feedback(
            self,
            session: AsyncSession,
            user: FeedbackCreateUpdateSchema,
    ) -> FeedbackSchema:
        query = (
            insert(self._collection)
            .values(user.model_dump())
            .returning(self._collection)
        )
        created_user = await session.scalar(query)
        await session.flush()

        return FeedbackSchema.model_validate(obj=created_user)

    async def update_feedback(
            self,
            session: AsyncSession,
            id_coment: int,
            feedback: FeedbackCreateUpdateSchema,
    ) -> FeedbackSchema:
        query = (
            update(self._collection)
            .where(self._collection.id == id_coment)
            .values(feedback.model_dump())
            .returning(self._collection)
        )
        updated_feedback = await session.scalar(query)
        if not updated_feedback:
            raise intNotFound(_object="id_coment",_id=id_coment)
        return FeedbackSchema.model_validate(obj=updated_feedback)

    async def delete_feedback(
            self,
            session: AsyncSession,
            id_coment: int
    ) -> None:
        query = delete(self._collection).where(self._collection.id == id_coment)
        result = await session.execute(query)
        if not result.rowcount:
            raise intNotFound(_object="id_coment",_id=id_coment)