n= int(input("enter no of element"))

arr = []
for i in range (0 , n-1): 
   
   a= int(input("enter element"))
   arr.append(a)

t = n* (n+1)//2

s = sum(arr)
ele = t-s 
print("the element which is missing is " , ele)