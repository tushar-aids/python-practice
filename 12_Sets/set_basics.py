# Creating a set
fruits = {"apple", "banana", "mango", "apple"}

# Sets automatically remove duplicates
print("Fruits Set:", fruits)

# Adding elements
fruits.add("orange")
print("After adding orange:", fruits)

# Removing elements
fruits.remove("banana")
print("After removing banana:", fruits)

# Membership test
print("Is mango in fruits?", "mango" in fruits)
print("Is kiwi in fruits?", "kiwi" in fruits)

# Creating empty set (Important!)
empty_set = set()
print("Type of empty_set:", type(empty_set))



# output:
# Fruits Set: {'banana', 'apple', 'mango'}
# After adding orange: {'banana', 'apple', 'mango', 'orange'}
# After removing banana: {'apple', 'mango', 'orange'}
# Is mango in fruits? True
# Is kiwi in fruits? False
# Type of empty_set: <class 'set'>
