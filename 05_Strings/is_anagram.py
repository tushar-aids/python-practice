# Check if two strings are anagrams

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Compare sorted characters
    return sorted(str1) == sorted(str2)

# Test cases
pairs = [
    ("listen", "silent"),
    ("race", "care"),
    ("hello", "world"),
    ("python", "typhon"),
    ("school master", "the classroom"),
]

for s1, s2 in pairs:
    result = is_anagram(s1, s2)
    print(f"'{s1}' & '{s2}' → Anagram: {result}")


# output:
# 'listen' & 'silent' → Anagram: True
# 'race' & 'care' → Anagram: True
# 'hello' & 'world' → Anagram: False
# 'python' & 'typhon' → Anagram: True
# 'school master' & 'the classroom' → Anagram: True
