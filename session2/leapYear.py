#Leap Year Checker
#Write a Python program that checks if a given year is a leap year. (A year is a leap year if it is divisible by 4 but not by 100, except when divisible by 400.)

year=2004
if (year%4==0 and year%100!=0)or year%400==0:
    print(year,"is leap year")
else:
    print("not leap year")
