from pydantic import BaseModel, Field


class ExpenseSchema(BaseModel):
    amount : float
    description : str = Field(min_length=3, max_length=100)