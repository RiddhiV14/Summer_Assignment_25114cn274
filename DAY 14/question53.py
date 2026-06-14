n= int(input("enter no of element"))
arr = []
for i in range (0 , n): 
   
   a= int(input("enter element"))
   arr.append(a)
ele = int(input("element to be found"))
pos = -1
for i in arr:
   pos = pos +1
   if i == ele :
      print("element is found at index",pos)
      break   
else: print("not found")   
      
    