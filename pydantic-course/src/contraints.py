from typing_extensions import Annotated
from pydantic import BaseModel, Field
from devtools import debug 

# use of Annotated is best practice 

class User(BaseModel):
    id: Annotated[int, Field(gt=0)]  
    name: Annotated[str, Field(max_length=10)]
    role: str = Field(max_length=10, description="role")

user = User(
    id=1,
    name="raj",
    role="designer"
)

debug(user)
