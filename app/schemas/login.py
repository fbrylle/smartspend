from pydantic import BaseModel, SecretStr, Field, field_validator


class LoginSchema(BaseModel):
    username : str = Field(max_length=100)
    password : SecretStr = Field(max_length=100)
    

    @field_validator('username', mode='after')
    @classmethod
    def check_username_input(cls, username):
        if len(username) <= 2:
            raise ValueError('Incorrect email or password')
        return username
    

    @field_validator('password', mode='after')
    @classmethod
    def password_input(cls, password: SecretStr):
        if len(password.get_secret_value()) <= 8:
            raise ValueError('Incorrect email or password')
        return password
        