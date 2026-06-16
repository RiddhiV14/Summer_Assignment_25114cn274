n= int(input("enter no of element"))

arr = []
for i in range (0 , n): 
   
   a= int(input("enter element"))
   arr.append(a)
max = 0
ele = arr[0]

for i in range(n) : 
    count = 0
    for j in range(n):
        if arr[i] == arr[j]:
            count = count +1 
    if count > max :
        max = count
        ele = arr[i]      

print ("max freq element is " , ele , "the freq is " , max )