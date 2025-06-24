import copy

# Shallow Copy Example
list1 = [[1, 2], [3, 4]]
shallow_copy = list1.copy()

shallow_copy[0][0] = 99

print("Original List (after shallow copy change):", list1)
print("Shallow Copy:", shallow_copy)

# Deep Copy Example
list2 = [[10, 20], [30, 40]]
deep_copy = copy.deepcopy(list2)

deep_copy[0][0] = 77

print("\nOriginal List (after deep copy change):", list2)
print("Deep Copy:", deep_copy)



# output:
# Original List (after shallow copy change): [[99, 2], [3, 4]]
# Shallow Copy: [[99, 2], [3, 4]]

# Original List (after deep copy change): [[10, 20], [30, 40]]
# Deep Copy: [[77, 20], [30, 40]]
