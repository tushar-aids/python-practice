# Normal set (mutable)
normal_set = {1, 2, 3}
normal_set.add(4)
print("Normal Set (after add):", normal_set)

# Frozen set (immutable)
frozen = frozenset([1, 2, 3])
print("Frozen Set:", frozen)

# Trying to add element to frozenset → Error
try:
    frozen.add(4)
except AttributeError as e:
    print("Error (cannot modify frozenset):", e)

# Using frozenset as dictionary key
my_dict = {frozenset([1, 2]): "valid key"}
print("Dictionary using frozenset as key:", my_dict)



# output:
# Normal Set (after add): {1, 2, 3, 4}
# Frozen Set: frozenset({1, 2, 3})
# Error (cannot modify frozenset): 'frozenset' object has no attribute 'add'
# Dictionary using frozenset as key: {frozenset({1, 2}): 'valid key'}
