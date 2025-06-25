# Creating a tuple
fruits = ("apple", "banana", "mango", "grapes")

# Accessing elements
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Slicing
print("First 2 fruits:", fruits[:2])

# Looping through a tuple
print("All fruits:")
for fruit in fruits:
    print(fruit)

# Length of tuple
print("Total fruits:", len(fruits))



# output:
# First fruit: apple
# Last fruit: grapes
# First 2 fruits: ('apple', 'banana')
# All fruits:
# apple
# banana
# mango
# grapes
# Total fruits: 4
