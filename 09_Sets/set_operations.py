A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# Union: all unique elements from both
union_set = A.union(B)
print("Union:", union_set)

# Intersection: common elements
intersection_set = A.intersection(B)
print("Intersection:", intersection_set)

# Difference: elements in A but not in B
difference_set = A.difference(B)
print("A - B:", difference_set)

# Symmetric Difference: elements in A or B but not both
symmetric_diff = A.symmetric_difference(B)
print("Symmetric Difference:", symmetric_diff)



# output:
# Union: {1, 2, 3, 4, 5, 6}
# Intersection: {3, 4}
# A - B: {1, 2}
# Symmetric Difference: {1, 2, 5, 6}
