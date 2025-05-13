# --------------------------- Lesson 08: Modules & Functions ---------------------------

# Creating a Module (mymodule.py) in the same file for simplicity

# Function to greet a user
def greet(name):
    return f"Hello, {name}!"

# Function to add two numbers
def add_numbers(a, b):
    return a + b

# Function to subtract two numbers
def subtract_numbers(a, b):
    return a - b

# Function to multiply two numbers
def multiply_numbers(a, b):
    return a * b

# Function to divide two numbers
def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

# --------------------------- Using the Functions and Module ---------------------------

# Calling the functions defined above in the same file

# Greet function example
print("------ Greet Function ------")
print(greet("Alice"))

# Add numbers function example
print("\n------ Add Numbers Function ------")
print(add_numbers(10, 5))

# Subtract numbers function example
print("\n------ Subtract Numbers Function ------")
print(subtract_numbers(10, 5))

# Multiply numbers function example
print("\n------ Multiply Numbers Function ------")
print(multiply_numbers(10, 5))

# Divide numbers function example
print("\n------ Divide Numbers Function ------")
print(divide_numbers(10, 5))
print(divide_numbers(10, 0))

