# JSON Schema dump compatible with OpenAPI 3.1

from datetime import datetime
from devtools import debug 
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    zipcode: str


class Meeting(BaseModel):
    when: datetime
    where: Address
    why: str = "No idea"


debug(Meeting.model_json_schema())
