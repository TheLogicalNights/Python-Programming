# Problem Statement :  Accept one number from user and print that number of * on screen. 

def Display(iNo):
    while(iNo>0):
        print("*")
        iNo-=1

def main():
    iNo = int(input("Enter a number :\n"))
    Display(iNo)

if __name__ == '__main__':
    main()