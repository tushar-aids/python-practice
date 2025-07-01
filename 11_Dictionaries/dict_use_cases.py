# 1. Word frequency counter
text = "python is fun and python is powerful"
words = text.split()

word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

print("Word Frequency:")
print(word_freq)

# 2. Storing student marks dynamically
students = {}
students["Tushar"] = {"math": 90, "science": 85}
students["Neha"] = {"math": 92, "science": 88}

print("\nStudent Marks:")
for name, subjects in students.items():
    print(f"{name}: {subjects}")

# 3. Counting item frequency from a list
items = ["apple", "banana", "apple", "orange", "banana", "apple"]
item_count = {}

for item in items:
    item_count[item] = item_count.get(item, 0) + 1

print("\nItem Frequency:")
print(item_count)



# output:
# Word Frequency:
# {'python': 2, 'is': 2, 'fun': 1, 'and': 1, 'powerful': 1}

# Student Marks:
# Tushar: {'math': 90, 'science': 85}
# Neha: {'math': 92, 'science': 88}

# Item Frequency:
# {'apple': 3, 'banana': 2, 'orange': 1}
