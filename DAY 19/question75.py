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
arr2 =[]
for i in range(row):
    row2=[]
    for j in range(col):
        row2.append(arr1[j][i])
    arr2.append(row2)
print("the transpose is" ,arr2)    