# --------------------------- Lesson 09: Exception Handling in Python ---------------------------

# Example 1: Handling Division by Zero
def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error! Division by zero is not allowed.")
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print("Division was successful.")
    finally:
        print("Execution completed.")

# Test cases for division
divide_numbers(10, 2)  # Normal division
divide_numbers(10, 0)  # Division by zero

# --------------------------- Handling Multiple Exceptions ---------------------------

# Example 2: Catching Different Exceptions
def calculate_age(year_of_birth):
    try:
        current_year = 2025
        age = current_year - year_of_birth
        if age < 0:
            raise ValueError("Year of birth cannot be in the future.")
        print(f"Your age is: {age}")
    except TypeError:
        print("Error! Please provide a valid number for the year.")
    except ValueError as ve:
        print(f"Error! {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Age calculation attempted.")

# Test cases for age calculation
calculate_age(2000)  # Valid year
calculate_age("2000")  # Invalid input (string instead of number)
calculate_age(2026)  # Year in the future

# --------------------------- Handling File Not Found Error ---------------------------

# Example 3: Handling FileNotFoundError
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error! The file {filename} does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("File operation attempted.")

# Test cases for reading file
read_file("existing_file.txt")  # File exists
read_file("non_existing_file.txt")  # File does not exist

# --------------------------- Raising an Exception ---------------------------

# Example 4: Manually Raising an Exception
def withdraw_money(balance, amount):
    try:
        if amount > balance:
            raise ValueError("Insufficient funds!")
        balance -= amount
        print(f"Withdrawal successful! New balance: {balance}")
    except ValueError as ve:
        print(f"Error: {ve}")
    finally:
        print("Withdrawal attempt completed.")

# Test cases for withdrawal
withdraw_money(1000, 500)  # Successful withdrawal
withdraw_money(1000, 1500)  # Insufficient funds

# --------------------------- Conclusion ---------------------------

# Exception handling ensures that errors are caught and dealt with, 
# preventing the program from crashing unexpectedly.

