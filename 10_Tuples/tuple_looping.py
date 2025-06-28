# Simple tuple
colors = ("red", "green", "blue")

# Loop through values
print("Colors:")
for color in colors:
    print(color)

# Loop with index using enumerate
print("\nColors with index:")
for index, color in enumerate(colors):
    print(f"{index}: {color}")

# Nested tuples
students = (
    ("Tushar", 21),
    ("Neha", 20),
    ("Amit", 22)
)

# Loop through nested tuples
print("\nStudent details:")
for name, age in students:
    print(f"Name: {name}, Age: {age}")



# output:
# Colors:
# red
# green
# blue

# Colors with index:
# 0: red
# 1: green
# 2: blue

# Student details:
# Name: Tushar, Age: 21
# Name: Neha, Age: 20
# Name: Amit, Age: 22
