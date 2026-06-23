s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagram Strings")
else:
    count = 0

    for ch in s1:
        if s1.count(ch) == s2.count(ch):
            count += 1

    if count == len(s1):
        print("Anagram Strings")
    else:
        print("Not Anagram Strings")