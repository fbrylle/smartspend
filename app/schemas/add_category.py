from pydantic import BaseModel, Field


class CategorySchema(BaseModel):
    name : str = Field(min_length=3, max_length=100)