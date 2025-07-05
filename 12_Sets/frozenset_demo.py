# Normal set (mutable)
normal_set = {"apple", "banana", "mango"}
normal_set.add("orange")  # works fine
print("Normal Set:", normal_set)

# Frozen set (immutable)
frozen = frozenset(["apple", "banana", "mango"])
print("Frozen Set:", frozen)

# frozen.add("orange") → Error
# Uncommenting below line will raise error
# frozen.add("orange")  # AttributeError

# Use-case: frozenset as dictionary key
location_data = {
    frozenset(["Pune", "Mumbai"]): "Maharashtra",
    frozenset(["Bangalore", "Mysore"]): "Karnataka"
}

print("\nAccessing using frozenset key:")
print(location_data[frozenset(["Pune", "Mumbai"])])



# output:
# Normal Set: {'apple', 'banana', 'mango', 'orange'}
# Frozen Set: frozenset({'apple', 'banana', 'mango'})

# Accessing using frozenset key:
# Maharashtra

