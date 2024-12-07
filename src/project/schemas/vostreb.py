from pydantic import BaseModel, ConfigDict


class VostrebSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_username: str
    id_meal: str
    count_obr: int

