from idlelib.squeezer import Squeezer

from fastapi import APIRouter

from project.infrastructure.postgres.repository.meals_repo import MealsRepository
from project.infrastructure.postgres.repository.country_repo import CountryRepository
from project.infrastructure.postgres.repository.cooking_repo import CookingRepository
from project.infrastructure.postgres.repository.feedback_repo import FeedbackRepository
from project.infrastructure.postgres.repository.ingredients_repo import IngredientsRepository
from project.infrastructure.postgres.repository.kbzu_repo import KbzuRepository
from project.infrastructure.postgres.repository.sostav_repo import SostavRepository
from project.infrastructure.postgres.repository.users_repo import UsersRepository
from project.infrastructure.postgres.repository.vostreb_repo import VostrebRepository


from project.infrastructure.postgres.database import PostgresDatabase
from project.schemas.meals import MealsSchema
from project.schemas.meals import MealsCreateUpdateSchema
from project.schemas.cooking import CookingSchema
from project.schemas.cooking import CookingCreateUpdateSchema
from project.schemas.country import CountrySchema
from project.schemas.country import CountryCreateUpdateSchema
from project.schemas.feedback import FeedbackSchema
from project.schemas.feedback import FeedbackCreateUpdateSchema
from project.schemas.ingredients import IngredientsSchema
from project.schemas.ingredients import IngredientsCreateUpdateSchema
from project.schemas.kbzu import KbzuCreateUpdateSchema
from project.schemas.kbzu import KbzuSchema
from project.schemas.sostav import SostavSchema
from project.schemas.sostav import SostavCreateUpdateSchema
from project.schemas.users import UsersSchema
from project.schemas.users import UsersCreateUpdateSchema
from project.schemas.vostreb import VostrebSchema
from project.schemas.vostreb import VostrebCreateUpdateSchema


router = APIRouter()

#meals
@router.get("/all_meals", response_model=list[MealsSchema])
async def get_all_meals() -> list[MealsSchema]:
    meals_repo = MealsRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await meals_repo.check_connection(session=session)
        all_meals = await meals_repo.get_all_meals(session=session)

    return all_meals
@router.get("/meal/{id}", response_model=MealsSchema)
async def get_meal_by_id(id_meal :str) -> MealsSchema:
    meals_repo = MealsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await meals_repo.check_connection(session=session)
        user = await meals_repo.get_meal_by_id(session=session, id=id_meal)
    return user
@router.post("/create_meal", response_model=MealsSchema)
async def create_meal(
    user_dto: MealsCreateUpdateSchema,
) -> MealsSchema:
    meals_repo = MealsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        new_meal = await meals_repo.create_meal(session=session, meal=user_dto)
    return new_meal
@router.put(
    "/update_meal/{id_meal}",
    response_model=MealsSchema,
)

async def update_meal(
    id_meal: str,
    user_dto: MealsCreateUpdateSchema,
) -> MealsSchema:
    user_repo = MealsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        updated_user = await user_repo.update_meal(
            session=session,
            id=id_meal,
            user=user_dto
        )
    return updated_user
@router.delete("/delete_meal/{id_meal}")
async def delete_user(id_meal :str) -> None:
    user_repo = MealsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await user_repo.check_connection(session=session)
        user = await user_repo.delete_meal(session=session, id=id_meal)
    return user









#cooking
@router.get("/all_sposobs", response_model=list[CookingSchema])
async def get_all_meals() -> list[CookingSchema]:
    cooking_repo = CookingRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await cooking_repo.check_connection(session=session)
        all_sposobs = await cooking_repo.get_all_cooking(session=session)

    return all_sposobs
@router.get("/sposob/{id}", response_model=CookingSchema)
async def get_meal_by_id(id_sposob :str) -> CookingSchema:
    cooking_repo = CookingRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await cooking_repo.check_connection(session=session)
        sposob = await cooking_repo.get_cooking_by_id(session=session, id_sposob=id_sposob)
    return sposob
@router.post("/create_sposob", response_model=CookingSchema)
async def create_meal(
    user_dto: CookingCreateUpdateSchema,
) -> CookingSchema:
    meals_repo = CookingRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        new_sposob = await meals_repo.create_sposob(session=session, sposob1=user_dto)
    return new_sposob
@router.put(
    "/update_sposob/{id_sposob}",
    response_model=MealsSchema,
)

async def update_meal(
    id_sposob: str,
    user_dto: CookingCreateUpdateSchema,
) -> CookingSchema:
    user_repo = CookingRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        updated_user = await user_repo.update_sposob(
            session=session,
            id_sposob=id_sposob,
            sposob=user_dto
        )
    return updated_user
@router.delete("/delete_sposob/{id_sposob}")
async def delete_user(id_sposob :str) -> None:
    user_repo = CookingRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await user_repo.check_connection(session=session)
        sposob = await user_repo.delete_sposob(session=session, id_sposob=id_sposob)
    return sposob




#country
@router.get("/all_country", response_model=list[CountrySchema])
async def get_all_country() -> list[CountrySchema]:
    country_repo = CountryRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await country_repo.check_connection(session=session)
        all_country = await country_repo.get_all_country(session=session)

    return all_country
@router.get("/country/{id}", response_model=CountrySchema)
async def get_country_by_id(id :int) -> CountrySchema:
    country_repo = CountryRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await country_repo.check_connection(session=session)
        sposob = await country_repo.get_country_id(session=session, id_country=id)
    return sposob
@router.post("/create_country_with_meal", response_model=CountrySchema)
async def create_country(
    user_dto: CountryCreateUpdateSchema,
) -> CountrySchema:
    country_repo = CountryRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        new_country = await country_repo.create_country(session=session, country=user_dto)
    return new_country
@router.put(
    "/update_country/{id}",
    response_model=CountrySchema,
)

async def update_country(
    id: int,
    user_dto: CountryCreateUpdateSchema,
) -> CountrySchema:
    country_repo = CountryRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        updated_country = await country_repo.update_country(
            session=session,
            id_country=id,
            country=user_dto
        )
    return updated_country
@router.delete("/delete_country/{id}")
async def delete_country(id :int) -> None:
    user_repo = CountryRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await user_repo.check_connection(session=session)
        sposob = await user_repo.delete_country(session=session, id_country=id)
    return sposob


#feedback
@router.get("/all_feedback", response_model=list[FeedbackSchema])
async def get_all_feedback() -> list[FeedbackSchema]:
    f_repo = FeedbackRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await f_repo.check_connection(session=session)
        all_f = await f_repo.get_all_feedback(session=session)

    return all_f
@router.get("/feedback/{id}", response_model=FeedbackSchema)
async def get_feedback_by_id(id :int) -> FeedbackSchema:
    f_repo = FeedbackRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        fe = await f_repo.get_feedback_by_id(session=session, id_coment=id)
    return fe
@router.post("/create_feedback", response_model=FeedbackSchema)
async def create_feedback(
    user_dto: FeedbackCreateUpdateSchema,
) -> FeedbackSchema:
    f_repo = FeedbackRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        new_f = await f_repo.create_feedback(session=session, user=user_dto)
    return new_f
@router.put(
    "/update_feedback/{id}",
    response_model=FeedbackSchema,
)

async def update_feedback(
    id: int,
    user_dto: FeedbackCreateUpdateSchema,
) -> FeedbackSchema:
    f_repo = FeedbackRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        updated_feedback = await f_repo.update_feedback(
            session=session,
            id_coment=id,
            feedback=user_dto
        )
    return updated_feedback
@router.delete("/delete_feedback/{id}")
async def delete_feedback(id :int) -> None:
    f_repo = FeedbackRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        f = await f_repo.delete_feedback(session=session, id_coment=id)
    return f



#ingredients
@router.get("/all_ing", response_model=list[IngredientsSchema])
async def get_all_ing() -> list[IngredientsSchema]:
    i_repo = IngredientsRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await i_repo.check_connection(session=session)
        all_i = await i_repo.get_all_ingredients(session=session)

    return all_i
@router.get("/ingredient/{id}", response_model=IngredientsSchema)
async def get_ing_by_id(id :str) -> IngredientsSchema:
    i_repo = IngredientsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await i_repo.check_connection(session=session)
        ing = await i_repo.get_ing_by_id(session=session, id=id)
    return ing
@router.post("/create_ing", response_model=IngredientsSchema)
async def create_ing(
    user_dto: IngredientsCreateUpdateSchema,
) -> IngredientsSchema:
    i_repo = IngredientsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        new_i = await i_repo.create_ing(session=session, ing=user_dto)
    return new_i
@router.put(
    "/update_ing/{id}",
    response_model=IngredientsSchema,
)

async def update_ing(
    id: str,
    user_dto: IngredientsCreateUpdateSchema,
) -> IngredientsSchema:
    i_repo = IngredientsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        updated_feedback = await i_repo.update_ing(
            session=session,
            id=id,
            user=user_dto
        )
    return updated_feedback
@router.delete("/delete_ing/{id}")
async def delete_ing(id :str) -> None:
    i_repo = IngredientsRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await i_repo.check_connection(session=session)
        i = await i_repo.delete_ing(session=session, id=id)
    return i

#kbzu
@router.get("/all_kbzu", response_model=list[KbzuSchema])
async def get_all_kbzu() -> list[KbzuSchema]:
    kbzu_repo = KbzuRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await kbzu_repo.check_connection(session=session)
        all_f = await kbzu_repo.get_all_kbzu(session=session)

    return all_f
@router.get("/kbzu/{id}", response_model=KbzuSchema)
async def get_kbzu_by_id(id :int) -> KbzuSchema:
    f_repo = KbzuRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        fe = await f_repo.get_kbzu_by_id(session=session, id=id)
    return fe
@router.post("/create_kbzu", response_model=KbzuSchema)
async def create_kbzu(
    user_dto: KbzuCreateUpdateSchema,
) -> KbzuSchema:
    f_repo = KbzuRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        new_f = await f_repo.create_kbzu(session=session, user=user_dto)
    return new_f
@router.put(
    "/update_kbzu/{id}",
    response_model=KbzuSchema,
)

async def update_kbzu(
    id: int,
    user_dto: KbzuCreateUpdateSchema,
) -> KbzuSchema:
    f_repo = KbzuRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        updated_kbzu = await f_repo.update_kbzu(
            session=session,
            id=id,
            user=user_dto
        )
    return updated_kbzu
@router.delete("/delete_kbzu/{id}")
async def delete_kbzu(id :int) -> None:
    f_repo = KbzuRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        f = await f_repo.delete_kbzu(session=session, id=id)
    return f

#sostav
@router.get("/all_sostav", response_model=list[SostavSchema])
async def get_all_sostav() -> list[SostavSchema]:
    f_repo = SostavRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await f_repo.check_connection(session=session)
        all_f = await f_repo.get_all_sostav(session=session)

    return all_f
@router.get("/sostav/{id}", response_model=SostavSchema)
async def get_sostav_by_id(id :int) -> SostavSchema:
    f_repo = SostavRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        fe = await f_repo.get_sostav_by_id(session=session, id=id)
    return fe
@router.post("/create_sostav", response_model=FeedbackSchema)
async def create_sostav(
    user_dto: SostavCreateUpdateSchema,
) -> SostavSchema:
    f_repo = SostavRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        new_f = await f_repo.create_sostav(session=session, sostav=user_dto)
    return new_f
@router.put(
    "/update_sostav/{id}",
    response_model=SostavSchema,
)

async def update_sostav(
    id: int,
    user_dto: SostavCreateUpdateSchema,
) -> SostavSchema:
    f_repo = SostavRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        updated_feedback = await f_repo.update_sostav(
            session=session,
            id=id,
            user=user_dto
        )
    return updated_feedback
@router.delete("/delete_sostav/{id}")
async def delete_sostav(id :int) -> None:
    f_repo = SostavRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        f = await f_repo.delete_sostav(session=session, id=id)
    return f


#users
@router.get("/all_users", response_model=list[UsersSchema])
async def get_all_users() -> list[UsersSchema]:
    f_repo = UsersRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await f_repo.check_connection(session=session)
        all_f = await f_repo.get_all_users(session=session)

    return all_f
@router.get("/users/{id}", response_model=UsersSchema)
async def get_users_by_id(id :str) -> UsersSchema:
    f_repo = UsersRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        fe = await f_repo.get_user_by_id(session=session, user_id=id)
    return fe
@router.post("/create_users", response_model=UsersSchema)
async def create_users(
    user_dto: UsersCreateUpdateSchema,
) -> UsersSchema:
    f_repo = UsersRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        new_f = await f_repo.create_user(session=session, user=user_dto)
    return new_f
@router.put(
    "/update_user/{id}",
    response_model=UsersSchema,
)

async def update_users(
    id: str,
    user_dto: UsersCreateUpdateSchema,
) -> UsersSchema:
    f_repo = UsersRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        updated_feedback = await f_repo.update_user(
            session=session,
            user_id=id,
            user=user_dto
        )
    return updated_feedback
@router.delete("/delete_user/{id}")
async def delete_user(id :str) -> None:
    f_repo = UsersRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        f = await f_repo.delete_user(session=session, user_id=id)
    return f

#vostreb
@router.get("/all_vostreb", response_model=list[VostrebSchema])
async def get_all_vostreb() -> list[VostrebSchema]:
    f_repo = VostrebRepository()
    database = PostgresDatabase()

    async with database.session() as session:
        await f_repo.check_connection(session=session)
        all_f = await f_repo.get_all_vostreb(session=session)

    return all_f
@router.get("/vostreb/{id}", response_model=VostrebSchema)
async def get_vostreb_by_id(id :int) -> VostrebSchema:
    f_repo = VostrebRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        fe = await f_repo.get_vostreb_by_id(session=session, id=id)
    return fe
@router.post("/create_vostreb", response_model=VostrebSchema)
async def create_vostreb(
    user_dto: VostrebCreateUpdateSchema,
) -> VostrebSchema:
    f_repo = VostrebRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        new_f = await f_repo.create_vostreb(session=session, vostreb=user_dto)
    return new_f
@router.put(
    "/update_vostreb/{id}",
    response_model=VostrebSchema,
)

async def update_vostreb(
    id: int,
    user_dto: VostrebCreateUpdateSchema,
) -> VostrebSchema:
    f_repo = VostrebRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        updated_feedback = await f_repo.update_vostreb(
            session=session,
            id=id,
            user=user_dto
        )
    return updated_feedback
@router.delete("/delete_vostreb/{id}")
async def delete_vostreb(id :int) -> None:
    f_repo = VostrebRepository()
    database = PostgresDatabase()
    async with database.session() as session:
        await f_repo.check_connection(session=session)
        f = await f_repo.delete_vostreb(session=session, id=id)
    return f
