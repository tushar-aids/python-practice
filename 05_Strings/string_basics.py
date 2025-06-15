# Basic string operations

name = "Tushar Pawar"

# 1. Length of string
print("Length of name:", len(name))

# 2. Accessing characters
print("First character:", name[0])
print("Last character:", name[-1])

# 3. String slicing
print("First name:", name[0:6])     # Tushar
print("Last name:", name[7:])       # Pawar

# 4. String in upper & lower case
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())

# 5. Check if string contains a word
print("Contains 'Pawar'?", "Pawar" in name)



#Length of name: 12
#First character: T
#Last character: r
#First name: Tushar
#Last name: Pawar
#Uppercase: TUSHAR PAWAR
#Lowercase: tushar pawar
#Contains 'Pawar'? True
