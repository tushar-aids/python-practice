# 1. Tuple for coordinates (fixed values)
location = (18.5204, 73.8567)  # Pune latitude & longitude
print("Coordinates:", location)

# 2. Tuple as dictionary key
person_location = {
    ("Tushar", 21): "Nashik",
    ("Neha", 20): "Pune"
}
print("Dictionary with tuple keys:", person_location)

# 3. Function returning multiple values using tuple
def get_student():
    name = "Amit"
    age = 22
    branch = "AI & DS"
    return name, age, branch

student = get_student()
print("Returned tuple:", student)

# Unpacking
name, age, branch = get_student()
print(f"Name: {name}, Age: {age}, Branch: {branch}")



# output:
# Coordinates: (18.5204, 73.8567)
# Dictionary with tuple keys: {('Tushar', 21): 'Nashik', ('Neha', 20): 'Pune'}
# Returned tuple: ('Amit', 22, 'AI & DS')
# Name: Amit, Age: 22, Branch: AI & DS
