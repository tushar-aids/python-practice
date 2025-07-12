# Unpacking a tuple
person = ("Tushar", 20, "AI Student")
name, age, branch = person
print("Name:", name)
print("Age:", age)
print("Branch:", branch)

# Swapping two variables (Pythonic way)
a = 10
b = 5
a, b = b, a
print("\nAfter swapping: a =", a, ", b =", b)

# Loop unpacking from list of tuples
students = [("Neha", 21), ("Amit", 22), ("Sneha", 20)]
for name, age in students:
    print(f"{name} is {age} years old")

# Function returning multiple values using tuple
def get_stats():
    return (80, 90, 100)

maths, physics, cs = get_stats()
print("\nMarks:")
print("Maths:", maths)
print("Physics:", physics)
print("CS:", cs)



# output:
# Name: Tushar
# Age: 20
# Branch: AI Student

# After swapping: a = 5 , b = 10
# Neha is 21 years old
# Amit is 22 years old
# Sneha is 20 years old

# Marks:
# Maths: 80
# Physics: 90
# CS: 100
