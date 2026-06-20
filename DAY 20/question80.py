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

for i in range(col):
    b=0
    for j in range(row):
        
        b = b+ arr1[j][i]
    print(f"the sum of col{i+1} is{b} ")
    