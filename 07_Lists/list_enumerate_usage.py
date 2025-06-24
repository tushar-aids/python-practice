# Using enumerate() to access index + value together

fruits = ["apple", "banana", "mango", "grapes"]

# Basic enumerate usage
for index, fruit in enumerate(fruits):
    print(f"Index {index}: {fruit}")

# Start index from 1 instead of 0
print("\nIndexing from 1:")
for idx, fruit in enumerate(fruits, start=1):
    print(f"{idx}. {fruit}")



# output:
# Index 0: apple
# Index 1: banana
# Index 2: mango
# Index 3: grapes

# Indexing from 1:
# 1. apple
# 2. banana
# 3. mango
# 4. grapes
