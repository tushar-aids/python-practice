# Sorting using lambda on different types of data

# List of tuples (name, age)
people = [("Tushar", 21), ("Om", 20), ("Abhi", 22), ("Jay", 19)]

# Sort by age (2nd item in tuple)
sorted_by_age = sorted(people, key=lambda x: x[1])
print("Sorted by age:", sorted_by_age)

# Sort by name length
sorted_by_name_length = sorted(people, key=lambda x: len(x[0]))
print("Sorted by name length:", sorted_by_name_length)

# Sort by reverse age (highest first)
sorted_by_age_desc = sorted(people, key=lambda x: x[1], reverse=True)
print("Sorted by age descending:", sorted_by_age_desc)



# output:
# Sorted by age: [('Jay', 19), ('Om', 20), ('Tushar', 21), ('Abhi', 22)]
# Sorted by name length: [('Om', 20), ('Jay', 19), ('Abhi', 22), ('Tushar', 21)]
# Sorted by age descending: [('Abhi', 22), ('Tushar', 21), ('Om', 20), ('Jay', 19)]
