# Using all() and any() with lists

marks = [75, 80, 60, 90]
zeros = [0, 0, 0]
mixed = [0, 0, 85]

# all() – check if all elements are non-zero (True)
print("All passed:", all(marks))       # True
print("All zero:", all(zeros))         # False

# any() – check if any one element is non-zero (True)
print("Any non-zero (zeros):", any(zeros))   # False
print("Any non-zero (mixed):", any(mixed))   # True



# output:
# All passed: True
# All zero: False
# Any non-zero (zeros): False
# Any non-zero (mixed): True
