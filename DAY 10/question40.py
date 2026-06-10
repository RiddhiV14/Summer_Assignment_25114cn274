row = int(input("enter no of rows"))

for i in range (1, row +1):
    ch='A'
    for j in range (1 ,row-i+1):
        print(" " , end="")
    for j in range(1 , i+1):
        print(ch , end="")
        ch = chr(ord(ch)+1)  
    ch = chr(ord(ch) - 2)    
    for j in range(1 ,i ):
        print(ch , end="")  
        ch=chr(ord(ch)-1) 

    print()