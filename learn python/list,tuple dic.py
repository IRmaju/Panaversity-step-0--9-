# List banane ka tareeqa
my_list = [10, 20, 30, 40, 50]

# List mein item ko access karna
print(my_list[0])  # Pehla item print hoga, output: 10

# List mein item ko change karna
my_list[1] = 25
print(my_list)  # Output: [10, 25, 30, 40, 50]

# List mein item add karna
my_list.append(60)
print(my_list)  # Output: [10, 25, 30, 40, 50, 60]

# List mein item delete karna
del my_list[2]
print(my_list)  # Output: [10, 25, 40, 50, 60]

# Tuple banane ka tareeqa
my_tuple = (10, 20, 30, 40, 50)

# Tuple mein item ko access karna
print(my_tuple[1])  # Output: 20

# Tuples ko change nahi kar sakte (immutable hote hain), agar modify karna ho to list ka use karein


# Dictionary banane ka tareeqa
my_dict = {"name": "Ali", "age": 25, "city": "Karachi"}

# Dictionary mein value access karna
print(my_dict["name"])  # Output: Ali

# Dictionary mein item add karna
my_dict["profession"] = "Engineer"
print(my_dict)  # Output: {'name': 'Ali', 'age': 25, 'city': 'Karachi', 'profession': 'Engineer'}

# Dictionary mein item delete karna
del my_dict["age"]
print(my_dict)  # Output: {'name': 'Ali', 'city': 'Karachi', 'profession': 'Engineer'}
