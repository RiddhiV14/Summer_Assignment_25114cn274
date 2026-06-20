row = int(input("enter the no of rows"))
col = int(input("enter the no of col "))
arr1 = []
for i in range(row):
    row1=[]
    for j in range(col):
       a = int(input("enter the ele for M1"))
       row1.append(a)
    arr1.append(row1)   
print(arr1)
arr2 = []
for i in range(row):
    row3=[]
    for j in range(col):
       b = int(input("enter the ele for M2"))
       row3.append(b)
    arr2.append(row3)   
print(arr2)
arr3 =[]
for i in range(row):
    row2=[]
    for j in range (col):
        c = arr1[i][j]*arr2[i][j]
        row2.append(c)
    arr3.append(row2)    
print(arr3)        