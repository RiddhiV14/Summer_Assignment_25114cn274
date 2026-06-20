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

for i in range(row):
    b=0
    for j in range(col):
        
        b = b+ arr1[i][j]
    print(f"the sum of row{i+1} is{b} ")
    