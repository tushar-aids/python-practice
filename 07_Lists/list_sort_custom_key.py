# Sorting with custom key functions in list

names = ["Tushar", "Om", "Abhishek", "Ram", "Jay"]

# Sort by length of each name
sorted_by_length = sorted(names, key=len)
print("Sorted by length:", sorted_by_length)

# Sort by last character
sorted_by_last_char = sorted(names, key=lambda x: x[-1])
print("Sorted by last character:", sorted_by_last_char)

# Sort by second letter (if available)
sorted_by_second_letter = sorted(names, key=lambda x: x[1] if len(x) > 1 else "")
print("Sorted by second letter:", sorted_by_second_letter)



# output:
# Sorted by length: ['Om', 'Ram', 'Jay', 'Tushar', 'Abhishek']
# Sorted by last character: ['Tushar', 'Ram', 'Om', 'Abhishek', 'Jay']
# Sorted by second letter: ['Ram', 'Jay', 'Abhishek', 'Om', 'Tushar']
