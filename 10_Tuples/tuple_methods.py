# Tuple with repeated elements
numbers = (1, 2, 3, 2, 4, 2, 5)

# count(): kitni baar '2' aaya hai
count_2 = numbers.count(2)
print("Count of 2:", count_2)

# index(): pehli baar '2' kahan aaya hai
index_2 = numbers.index(2)
print("Index of first 2:", index_2)

# index() of an element not present (will give error)
try:
    print("Index of 99:", numbers.index(99))
except ValueError as e:
    print("Error:", e)



# output:
# Count of 2: 3
# Index of first 2: 1
# Error: tuple.index(x): x not in tuple
