n = int(input("Enter number of word: "))

names = []

for i in range(n):
    names.append(input("Enter words: "))

for i in range(n):
    for j in range(i + 1, n):
        if len(names[i]) > len(names[j]):
            names[i], names[j] = names[j], names[i]

print("Sorted :")
for name in names:
    print(name)