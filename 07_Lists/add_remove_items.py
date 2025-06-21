# Add, remove and update items in a list

numbers = [10, 20, 30, 40]

# Add
numbers.append(50)           # Add at end
numbers.insert(2, 25)        # Insert at index 2

# Remove
numbers.remove(20)           # Remove value 20
popped = numbers.pop()       # Remove last element

# Update
numbers[0] = 5               # Change 10 to 5

print("Updated list:", numbers)
print("Popped element:", popped)



# output:
# Updated list: [5, 25, 30, 40]
# Popped element: 50
