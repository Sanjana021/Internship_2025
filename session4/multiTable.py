""" Multiplication Table:
Create a Python program to print the multiplication table of any given number using a while loop.
 """


n=int(input("enter a number:"))
mul=1
while mul<=10:
    result=n*mul
    print(n,"*",mul,"=",result)
    mul+=1
    
