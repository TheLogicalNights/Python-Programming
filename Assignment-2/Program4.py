# Problem Statement : Accept two numbers from user and display first number in second 
# number of times.

def Display(iNo1,iNo2):
    for i in range(iNo2):
        print(iNo1)

def main():
    iNo1 = int(input("Enter first number :\n"))
    iNo2 = int(input("Enter first number :\n"))
    Display(iNo1,iNo2)

if __name__ == '__main__':
    main()