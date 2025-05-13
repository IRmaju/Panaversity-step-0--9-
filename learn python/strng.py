# Working with Strings
name = "Ali"  # String assignment
greeting = "Hello, " + name  # Concatenating strings
print(greeting)

# String methods
message = "Python is amazing!"
print(message.lower())  # Converts the string to lowercase
print(message.upper())  # Converts the string to uppercase
print(message.replace("amazing", "awesome"))  # Replaces a word in the string

# Type Casting
# Converting string to integer
num_str = "123"
num_int = int(num_str)
print(num_int + 5)  # Output: 128

# Converting integer to string
num = 456
num_str = str(num)
print("The number is: " + num_str)  # Output: The number is: 456

# Converting float to integer (Type casting)
float_num = 12.75
int_num = int(float_num)
print(int_num)  # Output: 12

# Converting integer to float
num = 42
float_num = float(num)
print(float_num)  # Output: 42.0
