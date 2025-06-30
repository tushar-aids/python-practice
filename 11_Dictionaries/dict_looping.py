student = {
    "name": "Tushar",
    "age": 22,
    "grade": "A"
}

# Loop through keys
print("Keys:")
for key in student:
    print(key)

# Loop through values
print("\nValues:")
for value in student.values():
    print(value)

# Loop through key-value pairs
print("\nKey-Value Pairs:")
for key, value in student.items():
    print(f"{key}: {value}")



# output:
# Keys:
# name
# age
# grade

# Values:
# Tushar
# 22
# A

# Key-Value Pairs:
# name: Tushar
# age: 22
# grade: A
