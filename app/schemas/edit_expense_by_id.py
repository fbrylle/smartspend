from pydantic import BaseModel, Field


class UpdateExpenseSchema(BaseModel):
    amount : int
    description : str = Field(min_length=3, max_length=100)