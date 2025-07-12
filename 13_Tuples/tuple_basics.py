# Creating a tuple
person = ("Tushar", 20, "AI Student")

# Indexing
print("Name:", person[0])
print("Age:", person[1])

# Slicing
print("Sliced tuple:", person[0:2])

# Length
print("Tuple Length:", len(person))

# Tuple with one item
one_item = ("hello",)
print("Single-item tuple:", one_item)
print("Type of one_item:", type(one_item))

# Tuple without comma → becomes string
not_tuple = ("hello")
print("Type of not_tuple:", type(not_tuple))



# outpput:
# Name: Tushar
# Age: 20
# Sliced tuple: ('Tushar', 20)
# Tuple Length: 3
# Single-item tuple: ('hello',)
# Type of one_item: <class 'tuple'>
# Type of not_tuple: <class 'str'>
