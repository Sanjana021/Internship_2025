num=int(input("Enter a number"))
temp=num
rev=0
while temp>0:
    rem=temp%10
    rev=(rev*10)+rem
    temp=temp//10
if rev!=num:
    print(num,"is not a palindrame")
else:
    print(num,"is a palindrome")
