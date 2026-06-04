start = int(input("Enter start: "))
end = int(input("Enter end: "))

print("Armstrong Numbers:")

for num in range(start, end + 1):
    temp = num
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if sum == num:
        print(num, end=" ")