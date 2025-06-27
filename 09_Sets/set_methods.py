A = {1, 2, 3}
B = {3, 4, 5}
C = {1, 2}

# update(): A me B ke elements add kar deta hai
A.update(B)
print("After update A with B:", A)

# copy(): new reference bana deta hai
original = {10, 20, 30}
copy_set = original.copy()
copy_set.add(40)
print("Original Set:", original)
print("Copied Set:", copy_set)

# isdisjoint(): returns True if no common elements
print("A and C disjoint?", A.isdisjoint(C))

# issubset(): returns True if C is completely inside A
print("Is C subset of A?", C.issubset(A))

# issuperset(): returns True if A contains all of C
print("Is A superset of C?", A.issuperset(C))



# output:
# After update A with B: {1, 2, 3, 4, 5}
# Original Set: {10, 20, 30}
# Copied Set: {40, 10, 20, 30}
# A and C disjoint? False
# Is C subset of A? True
# Is A superset of C? True
