# Reverse a given number

num = int(input("Enter a number: "))
reverse = 0
n = num  # original number preserve

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(f"Reverse of {num} is {reverse}")



# output:
# Enter a number: 1234
# Reverse of 1234 is 4321
