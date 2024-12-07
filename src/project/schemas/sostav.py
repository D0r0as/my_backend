from pydantic import BaseModel, ConfigDict


class SostavSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_sostav: int
    id_meal: str
    id_ingredient: str
    cnt: int
    ed_izm: str
    id_sposob: str

