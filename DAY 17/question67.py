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
    for j in arr2 :
        if i==j :
            arr3.append(i)
print(arr3)            