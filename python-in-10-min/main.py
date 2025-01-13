# Python Variables and Types
x = 10          # Integer
y = 3.14        # Float
name = "Alice"  # String
is_active = True # Boolean
print(type(x), type(y), type(name), type(is_active))  # Checking types

# Print and f-strings
print(f"Hello, {name}! You have {x} messages.")  # Formatted string

print("-------")

# If, Elif, Else
if x > 15:
    print("x is greater than 15")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is less than 10")

# For Loop with Range
for i in range(1, 6):  # Loops from 1 to 5
    print(f"Iteration {i}")

print("-------")
# Python Collections: List, Tuple, Dict
fruits = ["apple", "banana", "cherry"]  # List
coordinates = (10, 20, 30)              # Tuple (immutable)
person = {"name": "Bob", "age": 25}     # Dictionary

# accessing elements
print(fruits[0], coordinates[1], person["name"])

# list
fruits.append("orange")  
print(len(fruits))
print(fruits)

# dict
print(person.keys())
print(person.values())
for key, value in person.items():
    print(key, ":", value)

print("-------")

# Python Functions and Lambda
def add(a, b):
    return a + b

result = add(5, 7)
print(f"Sum: {result}")

square = lambda x: x * x  # Lambda function
print(f"Square: {square(4)}")

print("-------")

# Python Classes with __str__, __call__, and add method
class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, a, b):
        self.result = a + b
        return self.result

    def __call__(self, a, b):
        return self.add(a, b)

    def __str__(self):
        return f"Str invoked - Calculator result: {self.result}"
    
    def __repr__(self):
        return f"Repr invoked - Calculator result: {self.result}"
    
calc = Calculator()
print(calc.add(3, 5))     # Using add method
print(calc(7, 2))         # Using __call__ method
print(calc)               # Using __str__ to display the result, if both __str__ and __repr__, present then __str__ will take precendence, it is meant for user friendly message, __repr__ is for debugging. 
print(str(calc))          # calls __str__
print(repr(calc))         # calls __repr__

print("-------")

# File Handling using 'with'
with open("sample.txt", "w") as file:
    file.write("Hello, Python learners!")

with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

print("-------")

# try-except-finally 
try:
    num = int(input("Enter a number: "))
    if num < 0:
        raise ValueError("Number must be positive.")
    print(f"The result is {10 / num}")
except ValueError as e:
    print(f"ValueError: {e}")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("Execution finished.")

print("-------")

# Python Packages and Modules
import math
print(f"Square root of 16 is: {math.sqrt(16)}")

from utils import mymath # here, utils is package (folder with __init__.py file) and mymath is module
print(mymath.calcAdd(2,3))

from mymodule import c 
print(c())