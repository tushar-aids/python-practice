# Check if a number is an Armstrong number

num = int(input("Enter a number: "))
digits = str(num)
power = len(digits)
total = 0

for digit in digits:
    total += int(digit) ** power

if total == num:
    print(f"{num} is an Armstrong number")
else:
    print(f"{num} is not an Armstrong number")



# output:
# Enter a number: 153
# 153 is an Armstrong number
