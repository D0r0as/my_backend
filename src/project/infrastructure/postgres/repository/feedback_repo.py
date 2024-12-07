from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

from project.schemas.feedback import FeedbackSchema
from project.infrastructure.postgres.new_models import Feedback

from src.project.core.config import settings


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
        query = f"select * from {settings.POSTGRES_SCHEMA}.feedback;"

        feedback = await session.execute(text(query))

        return [FeedbackSchema.model_validate(obj=feedback) for feedback in feedback.mappings().all()]

