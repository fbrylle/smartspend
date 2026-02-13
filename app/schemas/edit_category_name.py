from pydantic import BaseModel, Field, field_validator


class CategoryUpdateSchema(BaseModel):
    name : str = Field(max_length=100)

    @field_validator('name', mode='after')
    @classmethod
    def name_must_not_empty(cls, v):
        if len(v) <= 2:
            raise ValueError('Category name should be atleast 3 characters long')
        return v
