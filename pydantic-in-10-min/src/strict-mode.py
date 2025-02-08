from datetime import datetime

from pydantic import BaseModel, ValidationError


class Meeting(BaseModel):
    when: datetime
    where: bytes


m = Meeting.model_validate({"when": "2020-01-01T12:00", "where": "home"})
print(m)

##########################################################

# try:
#     m = Meeting.model_validate(
#         {'when': '2020-01-01T12:00', 'where': 'home'}, strict=True
#     )
# except ValidationError as e:
#     print(e)

##########################################################

# m_json = Meeting.model_validate_json(
#     '{"when": "2020-01-01T12:00", "where": "home"}'
# )
# print(m_json)

# try:
#     m1 = Meeting.model_validate(m_json, strict=True)
# except ValidationError as e:
#     print(e)
