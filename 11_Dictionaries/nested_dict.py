# Dictionary containing other dictionaries
students = {
    "Tushar": {
        "age": 22,
        "grade": "A"
    },
    "Neha": {
        "age": 21,
        "grade": "B"
    },
    "Amit": {
        "age": 23,
        "grade": "A+"
    }
}

# Access nested value
print("Tushar's Grade:", students["Tushar"]["grade"])

# Loop through nested dictionary
print("\nAll student details:")
for name, info in students.items():
    print(f"Name: {name}")
    for key, value in info.items():
        print(f"  {key}: {value}")



# output:
# Tushar's Grade: A

# All student details:
# Name: Tushar
#   age: 22
#   grade: A
# Name: Neha
#   age: 21
#   grade: B
# Name: Amit
#   age: 23
#   grade: A+
