from pydantic import BaseModel, ConfigDict

class UsersCreateUpdateSchema(BaseModel):
    surname: str
    firstname: str
    fathername: str
    age: int
    gender: str
    country: str

class UsersSchema(UsersCreateUpdateSchema):
    model_config = ConfigDict(from_attributes=True)

    id_username: str


