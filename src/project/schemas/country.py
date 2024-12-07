from pydantic import BaseModel, ConfigDict

class CountryCreateUpdateSchema(BaseModel):
    id_country: str
    id_meal: str


class CountrySchema(CountryCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id:int

