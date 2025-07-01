student = {
    "name": "Tushar",
    "age": 22,
    "branch": "AI & DS"
}

# .keys() → returns all keys
print("Keys:", student.keys())

# .values() → returns all values
print("Values:", student.values())

# .items() → returns all (key, value) pairs
print("Items:", student.items())

# .get() → safely access value
print("Grade (using get):", student.get("grade", "Not assigned"))

# .update() → add or update multiple entries
student.update({"grade": "A", "age": 23})
print("After update:", student)

# .pop() → remove a key and return its value
removed_branch = student.pop("branch")
print("Removed branch:", removed_branch)
print("After pop:", student)



# output:
# Keys: dict_keys(['name', 'age', 'branch'])
# Values: dict_values(['Tushar', 22, 'AI & DS'])
# Items: dict_items([('name', 'Tushar'), ('age', 22), ('branch', 'AI & DS')])
# Grade (using get): Not assigned
# After update: {'name': 'Tushar', 'age': 23, 'branch': 'AI & DS', 'grade': 'A'}
# Removed branch: AI & DS
# After pop: {'name': 'Tushar', 'age': 23, 'grade': 'A'}
