from devtools import debug 

# Serialization
# - into dict
# - into dict with only jsonable fields
# - into json

from datetime import datetime

from pydantic import BaseModel


class Meeting(BaseModel):
    when: datetime
    where: bytes
    why: str = "No idea"


m = Meeting(when="2025-02-08T12:00", where="home")
debug(m.model_dump(exclude_unset=True))
debug(m.model_dump(exclude={"where"}, mode="json"))
debug(m.model_dump_json(exclude_defaults=True))
