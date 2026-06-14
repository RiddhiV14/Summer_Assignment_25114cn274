n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
l=arr[0]
sl=arr[0]
for i in arr:
    if l<i:
        l=i
for i in arr:     
    if (sl<i and i<l) :
        sl = i

print ("the sec largest no is" , sl)        

