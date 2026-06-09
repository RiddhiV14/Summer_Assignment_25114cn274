row =int(input("enter no of rows"))
a=1
for i in range(1,row+1):
    a=1
    for j in range(1,row-i+2):
        print(a, end =" ")
        a+=1
    print()    

