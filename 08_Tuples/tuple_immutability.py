# Tuple is immutable
colors = ("red", "green", "blue")

# Trying to modify a tuple (will raise error)
try:
    colors[0] = "yellow"    # Not allowed
except TypeError as e:
    print("Error:", e)

# But you can create a new tuple
new_colors = ("yellow",) + colors[1:]
print("New tuple:", new_colors)

# Tuple with mutable object inside (like list)
mixed = (1, [2, 3], 4)
mixed[1].append(5)
print("Tuple with list inside:", mixed)



# output:
# Error: 'tuple' object does not support item assignment
# New tuple: ('yellow', 'green', 'blue')
# Tuple with list inside: (1, [2, 3, 5], 4)
