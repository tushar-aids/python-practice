# Zipping and unzipping lists

names = ["Tushar", "Om", "Jay"]
scores = [85, 90, 78]

# Zip: Combine names with scores
combined = list(zip(names, scores))
print("Zipped List:", combined)

# Unzip: Separate names and scores again
unzipped_names, unzipped_scores = zip(*combined)
print("Unzipped Names:", list(unzipped_names))
print("Unzipped Scores:", list(unzipped_scores))



# output:
# Zipped List: [('Tushar', 85), ('Om', 90), ('Jay', 78)]
# Unzipped Names: ['Tushar', 'Om', 'Jay']
# Unzipped Scores: [85, 90, 78]
