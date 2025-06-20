# Check if a number is a palindrome

num = int(input("Enter a number: "))
n = num
reverse = 0

while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

if reverse == num:
    print(f"{num} is a palindrome number")
else:
    print(f"{num} is not a palindrome number")



# output:
# Enter a number: 121
# 121 is a palindrome number
