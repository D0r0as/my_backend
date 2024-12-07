from pydantic import BaseModel, ConfigDict


class UsersSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    surname: str
    firstname: str
    fathername: str
    id_username: str
    age: int
    gender: str
    country: str

