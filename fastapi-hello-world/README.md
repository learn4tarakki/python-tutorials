### About Fast API
 - extends Starlette
 - adds Security utilities + many more  

### Fast API depends on
 - Starlette (ASGI Framework - async server gateway interface)
 - Uvicorn (ASGI Server) - ASGI Framework run on ASGI Server 
 - Pydantic (Data Validation, Serialization and Documentation via JSON Schema)

## Fast API project 
- install uv
  - pipx install uv 
- uv init --app
- uv add fastapi --extra standard
- create main.py with '/' route serving {"Hello":"World"}
- run app using 
  - uv run fastapi dev
