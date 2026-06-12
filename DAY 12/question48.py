def perfect(n):
    s = 0

    for i in range(1, n):
        if n % i == 0:
            s = s + i

    if s == n:
        return "Perfect Number"
    else:
        return "Not Perfect Number"

x = int(input("Enter a number: "))
print(perfect(x))