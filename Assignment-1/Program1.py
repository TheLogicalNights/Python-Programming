# Problem Statement : Program to divide two numbers

iNo1 = int(input("Enter first number\n"))
iNo2 = int(input("Enter second numner\n"))
if(iNo2==0):
    print("Error : Unable to divide using zero")
else:
    division = iNo1//iNo2
    print("Division is :",division)