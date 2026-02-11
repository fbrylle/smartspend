from pydantic import BaseModel, SecretStr, Field, field_validator


class RegistrationSchema(BaseModel):
    fname : str = Field(min_length=2, max_length=55)
    lname : str = Field(min_length=2, max_length=55)
    username : str = Field(min_length=3, max_length=20)
    password : SecretStr = Field(max_length=100)

    @field_validator('password', mode='after')
    @classmethod
    def password_min_length(cls, v: SecretStr):
        if len(v.get_secret_value()) < 8:
            raise ValueError('Password must be at least 8 characters long')
        return v