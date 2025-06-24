# Removing duplicates from a list

numbers = [1, 2, 2, 3, 4, 4, 5]

# Method 1: Using set (unordered)
unique_set = list(set(numbers))
print("Using set:", unique_set)

# Method 2: Using loop (preserves order)
unique_loop = []
for num in numbers:
    if num not in unique_loop:
        unique_loop.append(num)
print("Using loop:", unique_loop)

# Method 3: Using dict.fromkeys() (preserves order in Python 3.7+)
unique_dict = list(dict.fromkeys(numbers))
print("Using dict.fromkeys():", unique_dict)



# output:
# Using set: [1, 2, 3, 4, 5]
# Using loop: [1, 2, 3, 4, 5]
# Using dict.fromkeys(): [1, 2, 3, 4, 5]
