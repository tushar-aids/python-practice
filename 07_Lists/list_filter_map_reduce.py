from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# Filter: Get even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", evens)

# Map: Square of all numbers
squares = list(map(lambda x: x ** 2, numbers))
print("Squares:", squares)

# Reduce: Sum of all numbers
total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", total)



# output:
# Even numbers: [2, 4, 6]
# Squares: [1, 4, 9, 16, 25, 36]
# Sum using reduce: 21
