# Nested tuple (2D data)
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

# Accessing individual elements
print("Top-left:", matrix[0][0])
print("Center:", matrix[1][1])
print("Bottom-right:", matrix[2][2])

# Looping through nested tuples
print("\nMatrix:")
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()  # new line after each row



# output:
# Top-left: 1
# Center: 5
# Bottom-right: 9

# Matrix:
# 1 2 3 
# 4 5 6 
# 7 8 9 
