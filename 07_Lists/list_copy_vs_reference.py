# Copy vs Reference in lists

original = [1, 2, 3]

# Reference copy
ref_copy = original
ref_copy[0] = 100

print("Original after reference change:", original)

# Real copy
original = [1, 2, 3]
real_copy = original[:]
real_copy[0] = 100

print("Original after real copy change:", original)



# output:
# Original after reference change: [100, 2, 3]
# Original after real copy change: [1, 2, 3]
