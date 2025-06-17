# Count frequency of each character in a string

def char_frequency(s):
    freq = {}

    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    return freq

# Test cases
text1 = "tushar"
text2 = "hello world"
text3 = "data science"

print(f"Frequency in '{text1}': {char_frequency(text1)}")
print(f"Frequency in '{text2}': {char_frequency(text2)}")
print(f"Frequency in '{text3}': {char_frequency(text3)}")



output:
Frequency in 'tushar': {'t': 1, 'u': 1, 's': 1, 'h': 1, 'a': 1, 'r': 1}
Frequency in 'hello world': {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
Frequency in 'data science': {'d': 1, 'a': 2, 't': 1, ' ': 1, 's': 1, 'c': 2, 'i': 1, 'e': 2, 'n': 1}
