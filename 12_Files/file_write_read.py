# Writing to a file
with open("example.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

# Reading from the file
with open("example.txt", "r") as f:
    content = f.read()
    print(content)



output:
First line
Second line
