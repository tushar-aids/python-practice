# 1. Word frequency counter (like word count in a sentence)
text = "ai ds ai python ai code ds python"
word_count = {}

for word in text.split():
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# 2. Grouping students by branch
students = [
    ("Neha", "AI"),
    ("Amit", "DS"),
    ("Sneha", "AI"),
    ("Tushar", "DS")
]

grouped = {}

for name, branch in students:
    if branch not in grouped:
        grouped[branch] = []
    grouped[branch].append(name)

print("\nStudents grouped by branch:")
for branch, names in grouped.items():
    print(f"{branch}: {names}")

# 3. Using defaultdict-like pattern (manual)
scores = {}
names = ["Tushar", "Neha", "Amit", "Tushar", "Neha"]

for name in names:
    scores[name] = scores.get(name, 0) + 10

print("\nScores by name:")
for name, score in scores.items():
    print(f"{name}: {score}")



# output:
# Word Frequency:
# ai: 3
# ds: 2
# python: 2
# code: 1

# Students grouped by branch:
# AI: ['Neha', 'Sneha']
# DS: ['Amit', 'Tushar']

# Scores by name:
# Tushar: 20
# Neha: 20
# Amit: 10
