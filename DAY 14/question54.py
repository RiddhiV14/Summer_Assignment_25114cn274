
n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    a = int(input("Enter element: "))
    arr.append(a)

ele = int(input("Enter element whose frequency is to be found: "))

count = 0

for i in arr:
    if i == ele:
        count = count + 1

print("Frequency of", ele, "is", count)