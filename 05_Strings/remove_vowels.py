# Remove vowels from a string

def remove_vowels(s):
    vowels = "aeiouAEIOU"
    result = ""

    for char in s:
        if char not in vowels:
            result += char

    return result

# Test cases
text1 = "Tushar Pawar"
text2 = "Python is Powerful"
text3 = "AEIOUaeiou"

print(f"Original: '{text1}' | Without vowels: '{remove_vowels(text1)}'")
print(f"Original: '{text2}' | Without vowels: '{remove_vowels(text2)}'")
print(f"Original: '{text3}' | Without vowels: '{remove_vowels(text3)}'")


# output:
# Original: 'Tushar Pawar' | Without vowels: 'Tshr Pwr'
# Original: 'Python is Powerful' | Without vowels: 'Pythn s Pwrl'
# Original: 'AEIOUaeiou' | Without vowels: ''
