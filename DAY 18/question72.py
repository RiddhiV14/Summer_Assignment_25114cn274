n = int(input("Enter number of elements: "))

arr = []
for i in range(n):
    arr.append(int(input("Enter element: ")))

for i in range(n - 1):
    for j in range(i + 1, n):
        if arr[i] < arr[j]:
            arr[i], arr[j] = arr[j], arr[i]

print("Descending order:", arr)