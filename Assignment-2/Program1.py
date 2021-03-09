# Problem Statement : Accept one number from user and print that number of * on screen
def Display(iNo):
    for i in range(iNo):
        print("*") 

def main():
    iNo = int(input("Enter a number : \n"))
    Display(iNo)

if __name__ == '__main__':
    main()