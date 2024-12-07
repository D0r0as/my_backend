from pydantic import BaseModel, ConfigDict

class CookingSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_sposob: str
    per_kkal: int
