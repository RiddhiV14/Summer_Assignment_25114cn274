f = input("enter string")
f1 = f
for ch in f:
    count = 0
    for c in f:
        if c ==ch :
            count += 1
    if count > 1:
        print(f"the freq of {ch} is {count}")    
