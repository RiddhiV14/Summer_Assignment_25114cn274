def arm(a):
    a1 =a
    count=0
    while a>0:
        
        count = count +1
        a=a//10
    a2=a1
    s=0
    while a1>0:
        
        s1 = a1%10 
        s = s + s1**count 
        a1= a1//10 

    if s==a2:
        return "is armstrong no"
    return"not armstrong" 
x = int(input("enter the no"))
output = arm(x)
print(output)