n = int(input("Enter no of elements: "))

arr = []
for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)

arr1 = []

for i in arr:
    if i not in arr1:
        arr1.append(i)

print(arr1)

