from datetime import datetime
from devtools import debug 

from pydantic import BaseModel, ValidationError


class Meeting(BaseModel):
    when: datetime
    where: bytes


m = Meeting.model_validate({"when": "2020-01-01T12:00", "where": "home"})
debug(m)

##########################################################

# try:
#     m = Meeting.model_validate(
#         {'when': '2020-01-01T12:00', 'where': 'home'}, strict=True
#     )
# except ValidationError as e:
#     debug(e)

##########################################################

# m_json = Meeting.model_validate_json(
#     '{"when": "2020-01-01T12:00", "where": "home"}'
# )
# debug(m_json)

# try:
#     m1 = Meeting.model_validate(m_json, strict=True)
# except ValidationError as e:
#     debug(e)
