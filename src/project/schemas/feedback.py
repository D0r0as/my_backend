from pydantic import BaseModel, ConfigDict
from datetime import date

class FeedbackSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id_coment: serial
    id_meal: str
    id_username: str
    mark: int
    coment: str
    dat: date

