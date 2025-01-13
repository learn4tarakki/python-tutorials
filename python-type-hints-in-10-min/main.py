############################################################################
# Built-in Type Hints
x: int = 10          # Integer
y: float = 3.14      # Float
name: str = "Alice"  # String
is_active: bool = True  # Boolean
print(f"x: {x}, y: {y}, name: {name}, is_active: {is_active}")

############################################################################
# Function with Type Hints
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet("Bob"))

############################################################################

# Using the typing Module for python 3.8+
from typing import List, Dict, Optional, Union, TypedDict

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5] 
# in 3.9+, numbers: list[int] = [1, 2, 3, 4, 5]

# Dictionary with string keys and integer values
person: Dict[str, int] = {"age": 30, "height": 175} 
# in 3.9+, person: dict[str, int] = {"age": 30, "height": 175}

# Several types 
result: Union[int, str] = 2 
# in 3.10+, result: int | str = 2
result = "hello"

# Optional type: value can be int or None
optional_value: Optional[int] = None # OR 
optional_value: Union[int, None] = None 
# in 3.10+, optional_value: int | None = None

# Printing examples
print(f"Numbers: {numbers}")
print(f"Person: {person}")
print(f"Optional value: {optional_value}")


# New Built-in Types in Python 3.9+
# List, Dict, and other types no longer need to be imported from typing
names: list[str] = ["Alice", "Bob", "Charlie"]  # List of strings
grades: dict[str, float] = {"Alice": 90.5, "Bob": 85.0}  # Dict with string keys and float values

print(f"Names: {names}")
print(f"Grades: {grades}")

############################################################################

# TypedDict - use only if for dictionaries with specific types of keys - prefer for dictionaries, not for classes 
class User(TypedDict):
    name: str
    age: int

# Example usage:
user: User = {"name": "Alice", "age": 30}

# Type Hints in Classes
class Calculator:
    def __init__(self) -> None:
        self.result: Optional[int] = None

    def add(self, a: int, b: int) -> int:
        self.result = a + b
        return self.result

    def __str__(self) -> str:
        return f"Result: {self.result}"

calc = Calculator()
print(calc.add(10, 20))
print(calc)

# Advance 
############################################################################

# DataClasses -  automatically generating methods like __init__, __repr__, and __eq__.
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    is_active: bool = True  # Default value for is_active

# Example usage:
user = User(name="Alice", age=30)
print(user)  # Output: User(name='Alice', age=30, is_active=True)

# The class is mutable by default:
user.age = 31
print(user.age)  # Output: 31

############################################################################

# Annotated is in typing in Python 3.9+. In 3.8+, it is part of typing_extensions module.
from typing import Annotated

def say_hello(name: Annotated[str, "this is just metadata"]) -> str:
    return f"Hello {name}"

############################################################################

# Generic Types Example (Simple)
from typing import TypeVar, Generic

# Define a generic type variable
T = TypeVar('T')

# A simple Box class that can hold any type of item
class Box(Generic[T]):
    def __init__(self, content: T) -> None:
        self.content = content

    def get_content(self) -> T:
        return self.content

# Example 1: Box holding an integer
int_box = Box(123)
print(f"Integer box contains: {int_box.get_content()}")

# Example 2: Box holding a string
str_box = Box("Hello, World!")
print(f"String box contains: {str_box.get_content()}")