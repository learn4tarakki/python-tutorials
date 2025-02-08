# Serialization
# - into dict
# - into dict with only jsonable fields 
# - into json 

from datetime import datetime

from pydantic import BaseModel


class Meeting(BaseModel):
    when: datetime
    where: bytes
    why: str = 'No idea'


m = Meeting(when='2025-02-08T12:00', where='home')
print(m.model_dump(exclude_unset=True))
print(m.model_dump(exclude={'where'}, mode='json'))
print(m.model_dump_json(exclude_defaults=True))