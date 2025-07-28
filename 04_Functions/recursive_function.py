def fact(n):
    # base case
    if n <= 1:
        return 1
    # recursive case
    return n * fact(n - 1)

num = 5
print("Factorial of", num, "is", fact(num))



output:
Factorial of 5 is 120
