from pydantic import BaseModel, ConfigDict

class KbzuSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_kbzu: int
    id_ingredient: str
    belki: float
    zhiri: float
    uglevodi: float
    kkal: float
