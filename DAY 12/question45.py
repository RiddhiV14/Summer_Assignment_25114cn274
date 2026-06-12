def pel(a):
    b= 0
    c=a
    while a != 0:
        a1 = a % 10
        b = b*10 + a1
        a = a//10
    if b == c :
        return print("is palandrom")   
    return print("not palandrom")
x = int(input("enter no "))
pel(x)