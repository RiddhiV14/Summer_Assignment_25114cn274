arr1 = []
arr2 = []
n1 = int(input("enter no of elements in arr 1"))
n2 = int(input("enter no of elements in arr 2"))
for i in range(n1):
    a = int(input("Enter element: "))
    arr1.append(a)
for i in range(n2):
    a = int(input("Enter element: "))
    arr2.append(a)    

merged = []

i = 0
j = 0

while i < len(arr1) and j < len(arr2):
    if arr1[i] <= arr2[j]:
        merged.append(arr1[i])
        i += 1
    else:
        merged.append(arr2[j])
        j += 1

while i < len(arr1):
    merged.append(arr1[i])
    i += 1

while j < len(arr2):
    merged.append(arr2[j])
    j += 1

print("Merged Array:", merged)