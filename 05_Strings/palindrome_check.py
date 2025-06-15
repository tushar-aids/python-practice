# Check if a string is a palindrome

def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Convert to lowercase and remove spaces
    return s == s[::-1]             # Compare with reversed string

# Test cases
word1 = "madam"
word2 = "Tushar"
word3 = "nurses run"

print(f"'{word1}' is palindrome?", is_palindrome(word1))
print(f"'{word2}' is palindrome?", is_palindrome(word2))
print(f"'{word3}' is palindrome?", is_palindrome(word3))


# Output:
# 'madam' is palindrome? True
# 'Tushar' is palindrome? False
# 'nurses run' is palindrome? True
