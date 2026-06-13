n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)

max = arr[0]
min = arr[0]
for i in arr:
    if max<i:
        max = i 
    if min> i :
        min = i 

print ("the min and max element is ", min , max)        