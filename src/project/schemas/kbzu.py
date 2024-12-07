from pydantic import BaseModel, ConfigDict


class KbzuCreateUpdateSchema(BaseModel):
    id_ingredient: str
    belki: float
    zhiri: float
    uglevodi: float
    kkal: float

class KbzuSchema(KbzuCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id_kbzu: int

