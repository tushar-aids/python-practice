# Tuple with repeated elements
numbers = (10, 20, 10, 30, 10, 40)

# Count how many times 10 appears
count_10 = numbers.count(10)
print("10 appears", count_10, "times")

# Index of first occurrence of 30
index_30 = numbers.index(30)
print("Index of 30:", index_30)

# If element not found (will raise error)
try:
    print("Index of 50:", numbers.index(50))
except ValueError:
    print("50 is not in the tuple")



# output:
# 10 appears 3 times
# Index of 30: 3
# 50 is not in the tuple
