n = int(input("enter no of elements"))
arr =[]
arr1 = []
for i in range (n):
    a= int(input("enter element"))
    arr.append(a)
for j in range (n-1,-1,-1):
         arr1.append(arr[j])
print(arr1)                
