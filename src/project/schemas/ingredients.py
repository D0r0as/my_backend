from pydantic import BaseModel, ConfigDict

class IngredientsSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_ingredient: str
    price: float
    ed_izm: str
