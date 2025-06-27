# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Initial set:", my_set)

# Sets automatically remove duplicates
dup_set = {1, 2, 2, 3, 4, 4, 5}
print("No duplicates allowed:", dup_set)

# Adding elements
my_set.add(6)
print("After adding 6:", my_set)

# Removing elements
my_set.remove(2)  # raises error if not present
print("After removing 2:", my_set)

# Safe removal using discard (no error)
my_set.discard(10)  # no error even if 10 not present
print("After discarding 10 (not present):", my_set)

# Length of set
print("Set size:", len(my_set))

# Clear all elements
my_set.clear()
print("After clear():", my_set)



# output:
# Initial set: {1, 2, 3, 4, 5}
# No duplicates allowed: {1, 2, 3, 4, 5}
# After adding 6: {1, 2, 3, 4, 5, 6}
# After removing 2: {1, 3, 4, 5, 6}
# After discarding 10 (not present): {1, 3, 4, 5, 6}
# Set size: 5
# After clear(): set()
