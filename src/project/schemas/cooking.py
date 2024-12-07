from pydantic import BaseModel, ConfigDict

class CookingCreateUpdateSchema(BaseModel):
    per_kkal: int

class CookingSchema(CookingCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id_sposob: str
