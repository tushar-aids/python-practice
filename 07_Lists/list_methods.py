# Demonstrate various list methods

data = [30, 10, 50]

data.append(40)            # Add 40 at end
data.extend([60, 70])      # Add multiple elements
data.insert(1, 20)         # Insert 20 at index 1

data.remove(10)            # Remove value 10
last = data.pop()          # Remove last and store it

data.sort()                # Sort list
data.reverse()             # Reverse list

print("Final list:", data)
print("Popped item:", last)

data.clear()               # Remove all items
print("Cleared list:", data)



# outpt:
# Final list: [70, 60, 50, 40, 30, 20]
# Popped item: 70
# Cleared list: []
