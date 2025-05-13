# Set banane ka tareeqa
my_set = {10, 20, 30, 40, 50}

# Set mein item ko access karna
# Set mein items ka order fix nahi hota, toh index ke through access nahi kar sakte
# Par aap directly item check kar sakte ho
print(20 in my_set)  # Output: True

# Set mein item add karna
my_set.add(60)
print(my_set)  # Output: {10, 20, 30, 40, 50, 60}

# Set mein item remove karna
my_set.remove(30)
print(my_set)  # Output: {10, 20, 40, 50, 60}

# Set mein duplicate items nahi hote
my_set.add(20)  # 20 already present hai, toh add nahi hoga
print(my_set)  # Output: {10, 20, 40, 50, 60}

# Set mein length dekhna
print(len(my_set))  # Output: 5


# Frozenset banane ka tareeqa
my_frozenset = frozenset([10, 20, 30, 40, 50])

# Frozenset mein item access karna
print(30 in my_frozenset)  # Output: True

# Frozenset ko modify nahi kar sakte (immutable hota hai)
# Agar koi item add ya remove karne ki koshish karenge, toh error aayega:
# my_frozenset.add(60)  # Error: 'frozenset' object has no attribute 'add'
# my_frozenset.remove(40)  # Error: 'frozenset' object has no attribute 'remove'

# Frozenset ko comparison mein use kiya ja sakta hai
set1 = frozenset([1, 2, 3])
set2 = frozenset([3, 2, 1])
print(set1 == set2)  # Output: True
