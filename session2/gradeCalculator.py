"""Grade Calculator
Take a student's marks as input and print their grade:
90 and above: A
80–89: B
70–79: C
60–69: D
Below 60: F
 """


mark=65
if mark>=90:
    print("A grade")
if mark>=80 and mark<=89:
    print("B grade")
if mark>=70 and mark<=79:
    print("C grade")
if mark>=60 and mark<=69:
    print("D grade")
if mark<60:
    print("F grade")
