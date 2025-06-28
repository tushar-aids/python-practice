import sys
import time

# List vs Tuple creation
my_list = [1, 2, 3, 4, 5]
my_tuple = (1, 2, 3, 4, 5)

# 1. Mutability
my_list[0] = 100  # This works

try:
    my_tuple[0] = 100  # This will raise error
except TypeError as e:
    print("Tuple is immutable:", e)

# 2. Memory usage
print("List size in bytes:", sys.getsizeof(my_list))
print("Tuple size in bytes:", sys.getsizeof(my_tuple))

# 3. Execution time
list_time_start = time.time()
for _ in range(1000000):
    temp = [1, 2, 3, 4, 5]
list_time_end = time.time()

tuple_time_start = time.time()
for _ in range(1000000):
    temp = (1, 2, 3, 4, 5)
tuple_time_end = time.time()

print("List creation time:", list_time_end - list_time_start)
print("Tuple creation time:", tuple_time_end - tuple_time_start)



# output:
# Tuple is immutable: 'tuple' object does not support item assignment
# List size in bytes: 96
# Tuple size in bytes: 80
# List creation time: 0.45
# Tuple creation time: 0.28
