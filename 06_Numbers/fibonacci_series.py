# Print Fibonacci series up to n terms

n = int(input("Enter number of terms: "))

a, b = 0, 1

print("Fibonacci series:")

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b



# output:
# Enter number of terms: 7
# Fibonacci series:
# 0 1 1 2 3 5 8
