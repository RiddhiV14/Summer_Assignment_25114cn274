n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter element: "))
    arr.append(num)
avg =0
sum =0
for i in arr:
    sum = i+sum
avg = sum //n 
print("sumof element is", sum)
print("average of elements is ", avg) 