s = input("enter string")

for ch in s:
    count = 0
    for c in s :
        if ch == c:
            count= count +1
    if count!=1 :
         print(f"the first repeting ch is {ch}")
         break    