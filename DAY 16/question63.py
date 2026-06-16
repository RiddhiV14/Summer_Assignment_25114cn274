n = int(input("Enter no of elements: "))

arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)

sum = int(input("Enter the sum: "))

print("Pairs giving sum are:")

for i in range(n):
    for j in range(i + 1, n):
        if arr[i] + arr[j] == sum:
            print(arr[i], arr[j])
         