from pydantic import BaseModel, SecretStr, Field


class LoginSchema(BaseModel):
    username : str = Field(min_length=3)
    password : SecretStr = Field(min_length=8, max_length=100)
    