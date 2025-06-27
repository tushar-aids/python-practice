# List allows duplicates
names_list = ["Tushar", "Tushar", "Amit", "Ravi"]
print("List:", names_list)

# Set removes duplicates automatically
names_set = set(names_list)
print("Set:", names_set)

# Membership test in list (slow for large data)
print("\nMembership Check:")
print("Amit in list?", "Amit" in names_list)
print("Amit in set?", "Amit" in names_set)

# Speed test (demo for logic, not actual time)
big_list = list(range(1000000)) + [999999]
big_set = set(big_list)

print("\nCheck 999999 in list and set:")
print(999999 in big_list)  # Slower
print(999999 in big_set)   # Faster




# output:
# List: ['Tushar', 'Tushar', 'Amit', 'Ravi']
# Set: {'Amit', 'Tushar', 'Ravi'}

# Membership Check:
# Amit in list? True
# Amit in set? True

# Check 999999 in list and set:
# True
# True
