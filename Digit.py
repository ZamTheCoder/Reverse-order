num = int(input("Enter your Number: "))

count = 0
while num > 0:
    count = count + 1
    num = num // 10

print("Total Number of digits =", count)