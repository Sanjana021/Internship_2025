""" Create a program that takes a user's age as input and prints:
"Child" if age < 12
"Teenager" if age is between 13 and 19
"Adult" if age is 20 or above."""


age=int(input("enter user's age:"))
if age<=12:
    print("Child")
if age>=13 and age<=19:
    print("Teenager")
else:
    print("Adult")
    
