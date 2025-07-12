student = {
    "name": "Tushar",
    "age": 21,
    "branch": "AI & DS",
    "cgpa": 8.2
}

# Loop through keys
print("Keys:")
for key in student:
    print(key)

# Loop through values
print("\nValues:")
for value in student.values():
    print(value)

# Loop through key-value pairs using items()
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")

# Loop with index using enumerate
print("\nWith Index:")
for index, (key, value) in enumerate(student.items()):
    print(f"{index+1}. {key} = {value}")



# output:
# Keys:
# name
# age
# branch
# cgpa

# Values:
# Tushar
# 21
# AI & DS
# 8.2

# Key-Value Pairs:
# name: Tushar
# age: 21
# branch: AI & DS
# cgpa: 8.2

# With Index:
# 1. name = Tushar
# 2. age = 21
# 3. branch = AI & DS
# 4. cgpa = 8.2
