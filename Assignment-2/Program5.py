# Problem Statement : Accept number from user and check whether number is even or 
# odd.

def EvenOdd(iNo):
    if(iNo%2==0):
        return True
    else:
        return False

def main():
    iNo = int(input("Enter a number :\n"))
    iRet = EvenOdd(iNo)
    if(iRet==True):
        print("{} is Even".format(iNo))
    else:
        print("{} is Odd".format(iNo))

if __name__ == '__main__':
    main()