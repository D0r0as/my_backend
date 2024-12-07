from pydantic import BaseModel, ConfigDict


class CountrySchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_country: str
    id_meal: str


