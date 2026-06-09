  
row = int(input("enter no of rows"))
ch = "A"
for i in range (1,row+1):
    for j in range (1 , row +2-i):
        print(ch , end=" ")
        

    print()
    ch = chr(ord(ch) + 1)