num=int(input("enter a number"))
while num>=10:
    temp=0
    while num>0:
        temp+=num%10
        num//=10
    num=temp
print("The sum is",num)









