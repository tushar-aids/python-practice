# Count alphabets, digits and special characters in a string

def check_char_types(s):
    alphabets = 0
    digits = 0
    special = 0

    for char in s:
        if char.isalpha():
            alphabets += 1
        elif char.isdigit():
            digits += 1
        else:
            special += 1

    return alphabets, digits, special

# Test cases
text1 = "Tushar123!"
text2 = "Hello@2025"
text3 = "1234567890"
text4 = "!!@#abcXYZ"

a1, d1, s1 = check_char_types(text1)
a2, d2, s2 = check_char_types(text2)
a3, d3, s3 = check_char_types(text3)
a4, d4, s4 = check_char_types(text4)

print(f"'{text1}' → Alphabets: {a1}, Digits: {d1}, Special: {s1}")
print(f"'{text2}' → Alphabets: {a2}, Digits: {d2}, Special: {s2}")
print(f"'{text3}' → Alphabets: {a3}, Digits: {d3}, Special: {s3}")
print(f"'{text4}' → Alphabets: {a4}, Digits: {d4}, Special: {s4}")




# output:
# 'Tushar123!' → Alphabets: 6, Digits: 3, Special: 1
# 'Hello@2025' → Alphabets: 5, Digits: 4, Special: 1
# '1234567890' → Alphabets: 0, Digits: 10, Special: 0
# '!!@#abcXYZ' → Alphabets: 6, Digits: 0, Special: 4
