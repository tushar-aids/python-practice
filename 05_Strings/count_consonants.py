# Count the number of consonants in a string

def count_consonants(s):
    s = s.lower()                     # Lowercase me convert
    vowels = "aeiou"
    count = 0

    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1

    return count

# Test cases
text1 = "Tushar Pawar"
text2 = "Python Programming"
text3 = "aeiou"

print(f"Consonants in '{text1}':", count_consonants(text1))
print(f"Consonants in '{text2}':", count_consonants(text2))
print(f"Consonants in '{text3}':", count_consonants(text3))


# output:
# Consonants in 'Tushar Pawar': 7
# Consonants in 'Python Programming': 13
# Consonants in 'aeiou': 0

