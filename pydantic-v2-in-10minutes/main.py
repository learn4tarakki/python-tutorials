from pydantic import BaseModel, Field, field_validator, ValidationError
from typing import Optional

# 1. Basic Pydantic model with Field for validation
class User(BaseModel):
    name: str = Field(..., max_length=50, description="The name of the user")  # Field with max length
    age: int = Field(..., gt=0, lt=120, description="Age must be between 1 and 119")  # Validating age range
    email: Optional[str] = Field(None, pattern=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', description="Valid email address")  # Optional email with regex validation

    # 2. Custom validation with a method
    @field_validator('name')
    @classmethod
    def check_name(cls, v):
        if not v.isalpha():
            raise ValueError('Name must only contain alphabetic characters.')
        return v

    # Custom method to validate age
    @field_validator('age')
    @classmethod
    def check_age(cls, v):
        if v < 18:
            raise ValueError('User must be at least 18 years old.')
        return v

# 3. Creating a valid User instance
try:
    user = User(name="Alice", age=30, email="alice@example.com")
    print("\nValid User:")
    print(user)
except ValidationError as e:
    print("\nValidation Error (Valid User):")
    print(e)

# 4. Creating an invalid User instance (age < 18)
try:
    invalid_user = User(name="Bob", age=17, email="bob@example.com")
except ValidationError as e:
    print("\nValidation Error (Invalid User - Age < 18):")
    print(e)

# 5. Creating an invalid User instance (non-alphabetic name)
try:
    invalid_user = User(name="Alice123", age=25, email="alice@example.com")
except ValidationError as e:
    print("\nValidation Error (Invalid User - Non-Alphabetic Name):")
    print(e)

# 6. Using Field with Default Values
class Product(BaseModel):
    name: str
    price: float = Field(..., gt=0, description="Price must be greater than 0")  # Product price validation
    description: Optional[str] = None  # Optional description field

# 7. Creating a valid Product instance
product = Product(name="Laptop", price=999.99)
print("\nValid Product:")
print(product)

# 8. Creating an invalid Product instance (price <= 0)
try:
    invalid_product = Product(name="Laptop", price=-50)
except ValidationError as e:
    print("\nValidation Error (Invalid Product - Price <= 0):")
    print(e)

# 9. Validating API-like responses (Simulating an API response validation)
class ApiResponse(BaseModel):
    status: str = Field(..., pattern=r"^(success|error)$", description="Status must be either 'success' or 'error'")
    data: Optional[dict] = None

# Simulating a valid API response
response = ApiResponse(status="success", data={"id": 1, "name": "Laptop"})
print("\nValid API Response:")
print(response)

# Simulating an invalid API response (invalid status)
try:
    invalid_response = ApiResponse(status="failure", data={"id": 1})
except ValidationError as e:
    print("\nValidation Error (Invalid API Response - Status):")
    print(e)
