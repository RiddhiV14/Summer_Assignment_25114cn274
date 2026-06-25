n = int(input("Enter number of names: "))

names = []

for i in range(n):
    names.append(input("Enter name: "))

for i in range(n):
    for j in range(i + 1, n):
        if names[i] > names[j]:
            names[i], names[j] = names[j], names[i]

print("Sorted names:")
for name in names:
    print(name)