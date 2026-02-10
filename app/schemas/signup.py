from pydantic import BaseModel, SecretStr, Field


class RegistrationSchema(BaseModel):
    fname : str = Field(min_length=2, max_length=55)
    lname : str = Field(min_length=2, max_length=55)
    username : str = Field(min_length=3, max_length=20)
    password : SecretStr = Field(min_length=8, max_length=100)