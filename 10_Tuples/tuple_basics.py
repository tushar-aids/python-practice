# Tuple creation
person = ("Tushar", 21, "AI & DS")

# Accessing elements
print("Name:", person[0])
print("Age:", person[1])
print("Branch:", person[2])

# Length of tuple
print("Length:", len(person))

# Tuple with one item (important edge case)
single_item = ("Python",)
print("Single-item tuple:", single_item)

# Without comma - not a tuple
not_tuple = ("Python")
print("Not a tuple, it's:", type(not_tuple))



output:
Name: Tushar
Age: 21
Branch: AI & DS
Length: 3
Single-item tuple: ('Python',)
Not a tuple, it's: <class 'str'>
