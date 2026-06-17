arr1 = [1, 2, 3, 4]
arr2 = [2, 3, 5]
arr3 = [2, 3, 6]

common = []

for i in arr1:
    if i in arr2 and i in arr3 and i not in common:
        common.append(i)

print("Common elements:", common)

