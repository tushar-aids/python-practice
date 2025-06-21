# Nested list (2D list) example

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Whole matrix:")
for row in matrix:
    print(row)

print("\nAccessing individual elements:")
print("Element at [0][1]:", matrix[0][1])
print("Element at [2][2]:", matrix[2][2])

print("\nPrinting matrix using nested loop:")
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(matrix[i][j], end=" ")
    print()



# output:
# Whole matrix:
# [1, 2, 3]
# [4, 5, 6]
# [7, 8, 9]

# Accessing individual elements:
# Element at [0][1]: 2
# Element at [2][2]: 9

# Printing matrix using nested loop:
# 1 2 3 
# 4 5 6 
# 7 8 9
