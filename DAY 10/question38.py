row= int(input("enter no of rows"))
for i in range (1 , row +1 ):
    for x in range(1 ,i ):
        print (" ", end =(""))   
    for y in range (1, 2*row-2*i+2):
        print("*" , end ="")
    print()
    