score = 0

print(" Quiz Application")

ans = input("Q1. What is the capital of India? ")
if ans.lower() == "delhi":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

ans = input("Q2. What is 5 + 3? ")
if ans == "8":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

ans = input("Q3. Which language is used for AI? ")
if ans.lower() == "python":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

print("\nYour Score =", score, "/3")