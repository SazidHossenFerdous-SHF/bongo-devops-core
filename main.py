a1=int(input("Enter the 1st Number: "))
a2=int(input("Enter the 2nd Number: "))
a3=int(input("Enter the 3rd Number: "))
a4=int(input("Enter the 4th Number: "))

if a1>a2:
    f1=a1
else:
    f1=a2

if a3>a4:
    f2=a3
else:
    f2=a4

if f1>f2:
    print("The Greatest Number is:",f1)
else:
    print("The Greatest Number is:",f2)
