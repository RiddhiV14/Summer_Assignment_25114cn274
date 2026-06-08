rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    ch = 'A'
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)
    print()