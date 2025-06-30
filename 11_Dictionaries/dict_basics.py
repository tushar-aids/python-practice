# Creating a dictionary
student = {
    "name": "Tushar",
    "age": 21,
    "branch": "AI & DS"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["grade"] = "A"
print("After adding grade:", student)

# Modifying existing value
student["age"] = 22
print("After modifying age:", student)

# Accessing a non-existent key (with get)
print("City (using get):", student.get("city", "Not found"))



# output:
# Name: Tushar
# Age: 21
# After adding grade: {'name': 'Tushar', 'age': 21, 'branch': 'AI & DS', 'grade': 'A'}
# After modifying age: {'name': 'Tushar', 'age': 22, 'branch': 'AI & DS', 'grade': 'A'}
# City (using get): Not found
