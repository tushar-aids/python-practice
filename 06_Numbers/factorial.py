# Find factorial of a number

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("Factorial of 0 is 1.")
else:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print(f"Factorial of {num} is {fact}")



# output:
# Enter a number: 5
# Factorial of 5 is 120
