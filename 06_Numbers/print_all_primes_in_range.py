# Print all prime numbers from 1 to n

n = int(input("Enter upper limit: "))

print(f"Prime numbers from 1 to {n} are:")

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")



# output:
# Enter upper limit: 20
# Prime numbers from 1 to 20 are:
# 2 3 5 7 11 13 17 19
