# Control Flow (if, elif, else)

age = 20

if age >= 18:
    print("You are an adult.")  # This will execute because age is 20
else:
    print("You are a minor.")

# Using elif to check multiple conditions
day = "Sunday"

if day == "Monday":
    print("Start of the week!")
elif day == "Friday":
    print("End of the work week!")
elif day == "Sunday":
    print("Relaxing day!")  # This will execute because day is Sunday
else:
    print("Midweek day.")

# Loops (for and while)

# For loop - Iterate through a range
for i in range(5):
    print(f"Iteration {i+1}")  # This will print Iteration 1 to Iteration 5

# For loop - Iterate through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I love {fruit}!")  # This will print "I love apple!", "I love banana!", "I love cherry!"

# While loop - Continue until condition is false
count = 0
while count < 3:
    print(f"Count is {count}")  # This will print Count is 0, 1, 2
    count += 1  # Incrementing count

# Using break and continue in loops

# Break - Stops the loop completely
for num in range(10):
    if num == 5:
        break  # This will stop the loop when num reaches 5
    print(num)  # This will print 0 to 4

# Continue - Skips the current iteration and moves to the next one
for num in range(5):
    if num == 2:
        continue  # This will skip the iteration when num is 2
    print(num)  # This will print 0, 1, 3, 4
