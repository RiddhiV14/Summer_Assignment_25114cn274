row = int(input("enter the no of rows"))
col = int(input("enter the no of col "))
if row != col:
    print("invalid")
else:    
    arr1 = []
    b=0
    for i in range(row):
     row1 = []
     for j in range(col):
         a = int(input("enter the ele for M1"))
         row1.append(a)
    arr1.append(row1)   
print(arr1)

for i in range(row):
    
    for j in range(col):
        if (i==j or i+j==row-1):
            b += arr1[i][j]

print("sum is ", b)