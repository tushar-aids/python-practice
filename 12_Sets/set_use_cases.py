# 1. Remove duplicates from list
cities = ["Pune", "Mumbai", "Delhi", "Pune", "Delhi"]
unique_cities = list(set(cities))
print("Unique Cities:", unique_cities)

# 2. Fast membership test (vs list)
names_list = ["Tushar", "Neha", "Amit", "Sneha"]
names_set = {"Tushar", "Neha", "Amit", "Sneha"}

print("\nList check (Rohit in list):", "Rohit" in names_list)
print("Set check (Rohit in set):", "Rohit" in names_set)

# 3. Find common elements between two lists
a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

common = set(a).intersection(b)
print("\nCommon Elements:", common)



# output:
# Unique Cities: ['Delhi', 'Pune', 'Mumbai']

# List check (Rohit in list): False
# Set check (Rohit in set): False

# Common Elements: {3, 4}
