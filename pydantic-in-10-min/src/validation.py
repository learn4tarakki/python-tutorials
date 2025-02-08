# class User: 
#     id: int
#     name: str 

# user = User(id="11", name="arjun") 
# print(user)

##############################

# class User: 
#     id: int
#     name: str 
#     def __init__(self,id,name):
#         self.id = id
#         self.name = name

# user = User(id="11", name="arjun") 
# print(user)

##############################

# from pydantic import BaseModel, ValidationError 

# class User(BaseModel): 
#     id: int
#     name: str 

# user = User(id="11", name="arjun") 
# print(user)

###############################

# from pydantic import BaseModel, ValidationError 

# class User(BaseModel): 
#     id: int
#     name: str 

# user_json = { "id": "1", "name": "arjun" } # from rest api call to external service

# try:
#     u = User(**user_json) 
#     print(u.model_dump()) 
# except ValidationError as e:
#     print(e.errors())