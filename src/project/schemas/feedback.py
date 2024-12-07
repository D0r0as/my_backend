from pydantic import BaseModel, ConfigDict
from datetime import date

class FeedbackCreateUpdateSchema(BaseModel):
    id_meal: str
    id_username: str
    mark: int
    coment: str
    dat: date


class FeedbackSchema(FeedbackCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id_coment: int


