# Find GCD and LCM of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# GCD logic using Euclidean algorithm
x, y = a, b
while y != 0:
    x, y = y, x % y
gcd = x

# LCM formula
lcm = (a * b) // gcd

print(f"GCD of {a} and {b} is {gcd}")
print(f"LCM of {a} and {b} is {lcm}")




# output:
# Enter first number: 12
# Enter second number: 18
# GCD of 12 and 18 is 6
# LCM of 12 and 18 is 36
