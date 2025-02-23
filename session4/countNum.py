num=int(input("enter a positive integer"))
count = 0
while num> 0:
    num //= 10
    count += 1
print(count)
