# List vs Tuple

# List (mutable)
my_list = [1, 2, 3]
my_list[0] = 10
my_list.append(4)
print("List:", my_list)

# Tuple (immutable)
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ❌ Error: Tuples are immutable
print("Tuple:", my_tuple)

# Length
print("List length:", len(my_list))
print("Tuple length:", len(my_tuple))



# output:
# List: [10, 2, 3, 4]
# Tuple: (1, 2, 3)
# List length: 4
# Tuple length: 3
