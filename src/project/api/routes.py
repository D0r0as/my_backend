from fastapi import APIRouter

from project.infrastructure.postgres.repository.meals_repo import MealsRepository
from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.meals import MealsSchema

#from src.project.schemas.meals import MealsSchema

router = APIRouter()

@router.get("/all_meals", response_model=list[MealsSchema])
async def get_all_meals() -> list[MealsSchema]:
    meals_repo = MealsRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await meals_repo.check_connection(session=session)
        all_meals = await meals_repo.get_all_meals(session=session)

    return all_meals