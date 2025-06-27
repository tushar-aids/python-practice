# Sample set
colors = {"red", "green", "blue"}

# Loop through set (unordered)
print("Colors:")
for color in colors:
    print(color)

# Membership testing
print("\nMembership Testing:")
print("red" in colors)      # True
print("yellow" in colors)   # False
print("yellow" not in colors)  # True

# Real-life use: checking access
allowed_users = {"admin", "tushar", "guest"}

user = "tushar"
if user in allowed_users:
    print(f"{user} is allowed.")
else:
    print(f"{user} is not allowed.")



# output:
# Colors:
# red
# blue
# green

# Membership Testing:
# True
# False
# True
# tushar is allowed.
