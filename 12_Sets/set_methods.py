# Sets of students
ds_students = {"Tushar", "Neha", "Amit"}
ml_students = {"Neha", "Amit", "Rohit"}

# Union → all unique elements from both
all_students = ds_students.union(ml_students)
print("Union:", all_students)

# Intersection → common elements
common_students = ds_students.intersection(ml_students)
print("Intersection:", common_students)

# Difference → only in ds_students
only_ds = ds_students.difference(ml_students)
print("Only in DS:", only_ds)

# Symmetric Difference → not common in both
not_common = ds_students.symmetric_difference(ml_students)
print("Not Common in Both:", not_common)

# Discard (safe remove)
ds_students.discard("Neha")
print("After discarding Neha from DS:", ds_students)

# Clear all elements
ml_students.clear()
print("After clearing ML set:", ml_students)



# output:
# Union: {'Tushar', 'Rohit', 'Neha', 'Amit'}
# Intersection: {'Neha', 'Amit'}
# Only in DS: {'Tushar'}
# Not Common in Both: {'Rohit', 'Tushar'}
# After discarding Neha from DS: {'Tushar', 'Amit'}
# After clearing ML set: set()
