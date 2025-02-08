from pydantic import BaseModel, Field, field_validator, ValidationError
from devtools import debug 

class User(BaseModel):
    name: str = Field(
        ..., max_length=50, description="The name of the user"
    )   
    @field_validator("name")
    @classmethod
    def check_name(cls, value):
        if not value.isalpha():
            raise ValueError("Name must only contain alphabetic characters.")
        return value

try:
    user = User(name="Alice123")
except ValidationError as e:
    debug("\nValidation Error (Invalid User - Non-Alphabetic Name):")
    debug(e.errors())