# Tuple of fruits
fruits = ("apple", "banana", "cherry", "mango")

# Normal loop
print("Fruits:")
for fruit in fruits:
    print(fruit)

# Loop with index using range
print("\nUsing index:")
for i in range(len(fruits)):
    print(f"Index {i} = {fruits[i]}")

# Loop with enumerate (best method)
print("\nUsing enumerate:")
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")



# output:
# Fruits:
# apple
# banana
# cherry
# mango

# Using index:
# Index 0 = apple
# Index 1 = banana
# Index 2 = cherry
# Index 3 = mango

# Using enumerate:
# 0: apple
# 1: banana
# 2: cherry
# 3: mango

