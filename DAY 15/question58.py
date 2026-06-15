n = int(input("Enter no of elements: "))

arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)

arr1 = [0] * n

for i in range(n - 1):
    arr1[i] = arr[i + 1]

arr1[n - 1] = arr[0]

print(arr1)

