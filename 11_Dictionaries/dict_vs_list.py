import time

# List of students
student_list = ["Tushar", "Neha", "Amit", "Rohit", "Sneha"]

# Dictionary of students with roll numbers
student_dict = {
    101: "Tushar",
    102: "Neha",
    103: "Amit",
    104: "Rohit",
    105: "Sneha"
}

# Search in list (slow)
start = time.time()
print("Tushar" in student_list)
end = time.time()
print("List Search Time:", end - start)

# Search in dictionary (fast)
start = time.time()
print(103 in student_dict)
end = time.time()
print("Dict Search Time:", end - start)



# output:
# True
# List Search Time: 4.0531e-06
# True
# Dict Search Time: 1.9073e-06
