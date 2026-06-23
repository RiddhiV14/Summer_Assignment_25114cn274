s = input("enter string")
cg=""
f=0
for ch in s:
    count = 0
    for c in s :
        if ch == c:
            count= count +1
    if count>f:
        f = count
        cg = ch
print(f"the most freq ch is {cg}")
             