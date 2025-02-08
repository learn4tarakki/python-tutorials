from typing_extensions import Annotated
from pydantic import BaseModel, Field
from devtools import debug 


class User(BaseModel):
    id: Annotated[int, Field(gt=0)]  # best practice, instead of using Field directly
    name: Annotated[str, Field(max_length=10)]


user = User(
    id=1,
    name="ms dhoni",
)

debug(user)
