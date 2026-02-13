from pydantic import BaseModel, Field, field_validator


class LoanSchema(BaseModel):
    name : str = Field(max_length=100)
    total_amount : int

    @field_validator('name', mode='after')
    @classmethod
    def name_length(cls, v):
        if len(v) <= 2:
            raise ValueError('Loan name must be atleast 3 characters long.')
        return v