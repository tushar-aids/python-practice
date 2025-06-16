# Count the number of vowels in a string

def count_vowels(s):
    s = s.lower()  # Convert string to lowercase
    vowels = "aeiou"
    count = 0

    for char in s:
        if char in vowels:
            count += 1

    return count

# Test cases
text1 = "Tushar Pawar"
text2 = "Python Programming"
text3 = "xyz"

print(f"Vowels in '{text1}':", count_vowels(text1))
print(f"Vowels in '{text2}':", count_vowels(text2))
print(f"Vowels in '{text3}':", count_vowels(text3))



# output:
# Vowels in 'Tushar Pawar': 4
# Vowels in 'Python Programming': 4
# Vowels in 'xyz': 0
