def reverse_num(n, rev=0):
    if n == 0:
        return rev
    return reverse_num(n // 10, rev * 10 + n % 10)

n = int(input("Enter a number: "))
print("Reverse =", reverse_num(n))