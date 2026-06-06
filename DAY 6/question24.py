x = int(input("Enter base (x): "))
n = int(input("Enter power (n): "))

result = 1

for i in range(n):
    result *= x

print("Answer =", result)