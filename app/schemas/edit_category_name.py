from pydantic import BaseModel, Field, field_validator


class CategoryUpdateSchema(BaseModel):
    name : str = Field(min_length=3, max_length=100)

    @field_validator('name')
    @classmethod
    def name_must_not_empty(cls, v):
        if not v.strip():
            raise ValueError('Category name cannot be empty.')
        return v.strip()
