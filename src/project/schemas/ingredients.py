from pydantic import BaseModel, ConfigDict


class IngredientsCreateUpdateSchema(BaseModel):
    price: float
    ed_izm: str

class IngredientsSchema(IngredientsCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id_ingredient: str

