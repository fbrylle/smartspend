from pydantic import BaseModel, Field, field_validator


class UpdateExpenseSchema(BaseModel):
    amount : int
    description : str = Field(max_length=100)

    @field_validator('description', mode='after')
    @classmethod
    def expense_description(cls, v):
        if len(v) <= 3:
            raise ValueError('Description should be atleast 4 characters long.')
        return v