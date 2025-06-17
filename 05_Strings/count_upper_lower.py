# Count uppercase and lowercase letters in a string

def count_upper_lower(s):
    upper = 0
    lower = 0

    for char in s:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1

    return upper, lower

# Test cases
text1 = "Tushar Pawar"
text2 = "PYTHON programming"
text3 = "12345!!!"

u1, l1 = count_upper_lower(text1)
u2, l2 = count_upper_lower(text2)
u3, l3 = count_upper_lower(text3)

print(f"'{text1}' → Uppercase: {u1}, Lowercase: {l1}")
print(f"'{text2}' → Uppercase: {u2}, Lowercase: {l2}")
print(f"'{text3}' → Uppercase: {u3}, Lowercase: {l3}")



# output:
# 'Tushar Pawar' → Uppercase: 2, Lowercase: 9
# 'PYTHON programming' → Uppercase: 6, Lowercase: 11
# '12345!!!' → Uppercase: 0, Lowercase: 0

