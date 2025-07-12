student = {
    "name": "Tushar",
    "age": 21,
    "branch": "AI & DS"
}

# 1. get() → safe way to access key
print("Name:", student.get("name"))
print("CGPA (not present):", student.get("cgpa", "Not Available"))

# 2. update() → add or modify keys
student.update({"cgpa": 8.2})
print("After update:", student)

# 3. keys(), values(), items()
print("\nAll keys:", list(student.keys()))
print("All values:", list(student.values()))
print("All items (key-value pairs):", list(student.items()))

# 4. clear() → delete all content
student.clear()
print("\nAfter clearing:", student)



# output:
# Name: Tushar
# CGPA (not present): Not Available
# After update: {'name': 'Tushar', 'age': 21, 'branch': 'AI & DS', 'cgpa': 8.2}

# All keys: ['name', 'age', 'branch', 'cgpa']
# All values: ['Tushar', 21, 'AI & DS', 8.2]
# All items (key-value pairs): [('name', 'Tushar'), ('age', 21), ('branch', 'AI & DS'), ('cgpa', 8.2)]

# After clearing: {}
