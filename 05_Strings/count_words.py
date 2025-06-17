# Count number of words in a sentence

def count_words(s):
    words = s.split()  # Split sentence by spaces into list
    return len(words)

# Test cases
sentence1 = "Tushar is learning Python"
sentence2 = "  Hello   world!  "
sentence3 = ""

print(f"Words in '{sentence1}':", count_words(sentence1))
print(f"Words in '{sentence2}':", count_words(sentence2))
print(f"Words in '{sentence3}':", count_words(sentence3))


# output:
# Words in 'Tushar is learning Python': 4
# Words in '  Hello   world!  ': 2
# Words in '': 0
