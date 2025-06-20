# Find the sum of digits of a number

num = int(input("Enter a number: "))
total = 0
n = num  # original number ko preserve karna

while n > 0:
    digit = n % 10
    total += digit
    n = n // 10

print(f"Sum of digits of {num} is {total}")



# output:
# Enter a number: 1234
# Sum of digits of 1234 is 10
