# List comprehension examples

# Squares of numbers
squares = [x**2 for x in range(1, 6)]

# Even numbers from list
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]

# Upper-case strings
names = ["tushar", "pawan", "raju"]
upper_names = [name.upper() for name in names]

print("Squares:", squares)
print("Even numbers:", evens)
print("Upper-case names:", upper_names)



# output:
# Squares: [1, 4, 9, 16, 25]
# Even numbers: [2, 4, 6]
# Upper-case names: ['TUSHAR', 'PAWAN', 'RAJU']
