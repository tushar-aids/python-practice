# Creating a dictionary
student = {
    "name": "Tushar",
    "age": 20,
    "branch": "AI & DS"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key
student["college"] = "SPPU"
print("After adding college:", student)

# Updating a value
student["age"] = 21
print("After updating age:", student)

# Deleting a key
del student["branch"]
print("After deleting branch:", student)



# output:
# Name: Tushar
# Age: 20
# After adding college: {'name': 'Tushar', 'age': 20, 'branch': 'AI & DS', 'college': 'SPPU'}
# After updating age: {'name': 'Tushar', 'age': 21, 'branch': 'AI & DS', 'college': 'SPPU'}
# After deleting branch: {'name': 'Tushar', 'age': 21, 'college': 'SPPU'}
