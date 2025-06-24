# Flattening a nested list

nested = [[1, 2], [3, 4], [5, 6]]
flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print("Flattened List:", flat)

# Using list comprehension
flat2 = [item for sublist in nested for item in sublist]
print("Flattened (Comprehension):", flat2)



# output:
# Flattened List: [1, 2, 3, 4, 5, 6]
# Flattened (Comprehension): [1, 2, 3, 4, 5, 6]
