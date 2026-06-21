s = input("enter string")
s1= s.upper()
v= ['A','E','I','O','U']
l = len(s)
count = 0
for a in s1 :
    for b in v:
        if a== b:
            count +=1
con = l - count
print(f"the no of vowels is {count} and consonent is {con}")        