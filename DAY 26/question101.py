import random

n1= random.randint(1,100)

while  True :
    n = int(input("enter no between 1 and 100"))
    if n1 > n :
        print("too low")
    elif n1< n :
        print ("too high")
    else :
        print("found it")    
        break