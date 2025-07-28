# Recursive function to find factorial

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calling the function
num = 5
print("Factorial of", num, "is", factorial(num))
