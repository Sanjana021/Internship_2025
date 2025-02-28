"""5.	Fibonacci Series:
Write a Python program to print the first n terms of the Fibonacci sequence using a while loop.
"""
num1=0
num2=1
print(num1)
print(num2)
for i in range(2,10):
    num3=num1+num2
    num1=num2
    num2=num3
    print(num3)
print()
    

