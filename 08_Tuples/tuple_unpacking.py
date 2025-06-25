# Tuple unpacking (assigning multiple variables)
person = ("Tushar", 20, "AI & DS")
name, age, branch = person

print("Name:", name)
print("Age:", age)
print("Branch:", branch)

# Swapping using tuple unpacking
a = 5
b = 10
a, b = b, a
print("\nAfter swapping:")
print("a =", a)
print("b =", b)

# Looping with unpacked tuples
students = [("Amit", 85), ("Neha", 90), ("Ravi", 78)]

print("\nStudent Marks:")
for name, marks in students:
    print(name, "scored", marks)



# output:
# Name: Tushar
# Age: 20
# Branch: AI & DS

# After swapping:
# a = 10
# b = 5

# Student Marks:
# Amit scored 85
# Neha scored 90
# Ravi scored 78
