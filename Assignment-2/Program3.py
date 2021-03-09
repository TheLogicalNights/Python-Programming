# Problem Statement :  Accept on number from user if number is less than 10 then print 
# “Hello” otherwise print “Demo”.  
def Check(iNo):
    if(iNo<10):
        print("Hello")
    else:
        print("Demo")

def main():
    iNo = int(input("Enter a number :\n"))
    Check(iNo)

if __name__ == '__main__':
    main()