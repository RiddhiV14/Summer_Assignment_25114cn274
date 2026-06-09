row = int(input("enter no of rows"))
for i in range(1,row+1):
    for j in range(1 , row-i+2):
        print("*" , end= '')
    print()


