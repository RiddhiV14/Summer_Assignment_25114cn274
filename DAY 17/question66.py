n1 = int(input("Enter size of first array: "))
arr1 = []

for i in range(n1):
    arr1.append(int(input("Enter element: ")))

n2 = int(input("Enter size of second array: "))
arr2 = []
arr3 = []
for i in range(n2):
    arr2.append(int(input("Enter element: ")))

for i in arr1:
    if i not in arr3:
        arr3.append(i)

for i in arr2:
    if i not in arr3:
        arr3.append(i)

print("Union =", arr3)        

