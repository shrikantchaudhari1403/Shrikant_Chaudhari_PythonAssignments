
checkEven= lambda num: num % 2 == 0

def main():
    num1= int(input("Enter a number: "))
    
    result= checkEven(num1)

    if result:
        print("The number is Even:", result)
    else:
        print("The number is Even:", result)

if __name__ == "__main__":
    main()