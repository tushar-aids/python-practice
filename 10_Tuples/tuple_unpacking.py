# Simple tuple
person = ("Tushar", 21, "AI & DS")

# Unpacking into variables
name, age, branch = person
print("Name:", name)
print("Age:", age)
print("Branch:", branch)

# Function that returns a tuple
def get_coordinates():
    return (10, 20)

x, y = get_coordinates()
print("X:", x)
print("Y:", y)

# Ignoring a value using _
student = ("Neha", 19, "AIDS")
name, _, branch = student
print("Name:", name)
print("Branch:", branch)



# output:
# Name: Tushar
# Age: 21
# Branch: AI & DS
# X: 10
# Y: 20
# Name: Neha
# Branch: AIDS
