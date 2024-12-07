from pydantic import BaseModel, ConfigDict

class VostrebCreateUpdateSchema(BaseModel):
    id_username: str
    id_meal: str
    count_obr: int

class VostrebSchema(VostrebCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id:int


