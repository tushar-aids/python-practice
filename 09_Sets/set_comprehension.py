# 1. Square of numbers from 1 to 5 using set comprehension
squares = {x ** 2 for x in range(1, 6)}
print("Squares Set:", squares)

# 2. Extract even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_set = {x for x in numbers if x % 2 == 0}
print("Even numbers Set:", even_set)

# 3. Convert list of names to lowercase (unique only)
names = ["Tushar", "Amit", "TUSHAR", "Neha"]
lowercase_names = {name.lower() for name in names}
print("Unique lowercase names:", lowercase_names)

# 4. First letters of all words (like hashtags, tags)
words = ["Python", "Programming", "Practice"]
first_letters = {word[0].upper() for word in words}
print("First letters set:", first_letters)



# output:
# Squares Set: {1, 4, 9, 16, 25}
# Even numbers Set: {2, 4, 6, 8}
# Unique lowercase names: {'tushar', 'neha', 'amit'}
# First letters set: {'P'}
