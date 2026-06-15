n = int(input("Enter no of elements: "))

arr = []

for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)

arr1 = [0] * n

j = 0

for i in range(n):
    if arr[i] != 0:
        arr1[j] = arr[i]
        j = j + 1

print(arr1)