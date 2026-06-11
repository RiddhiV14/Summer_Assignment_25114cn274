def prime (a):
    for i in range (2,int(a**0.5)+1):
        if a%i ==0:
            return "not prime"
            break 
        
        return "prime "

a1 = int(input("enter a no"))
out = prime (a1)
print(out)          