n = int(input("enter no of elements"))
arr =[]
first = 0
for i in range (n):
    a= int(input("enter element"))
    arr.append(a)
first = arr[n-1]    
for i in range(n):
    arr[i]=arr[i+1]    
arr[0]=first 
