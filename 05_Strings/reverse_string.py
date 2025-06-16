# Reverse a given string using slicing

def reverse_string(s):
    return s[::-1]  # Slice from end to start

# Test cases
word1 = "Tushar"
word2 = "Python"
word3 = "madam"

print("Original:", word1, "| Reversed:", reverse_string(word1))
print("Original:", word2, "| Reversed:", reverse_string(word2))
print("Original:", word3, "| Reversed:", reverse_string(word3))



# output:
# Original: Tushar | Reversed: rahsuT
# Original: Python | Reversed: nohtyP
# Original: madam | Reversed: madam
