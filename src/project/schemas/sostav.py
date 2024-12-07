from pydantic import BaseModel, ConfigDict

class SostavCreateUpdateSchema(BaseModel):
    id_meal: str
    id_ingredient: str
    cnt: int
    ed_izm: str
    id_sposob: str

class SostavSchema(SostavCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id_sostav: int


