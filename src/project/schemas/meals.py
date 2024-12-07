from pydantic import BaseModel, ConfigDict

class MealsCreateUpdateSchema(BaseModel):
    count_ingredients: int
    gruppa: str
    season: str
    weigth: int
    count_pors: int
    prepering_time: int

class MealsSchema(MealsCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id_meal: str
