

checkOdd= lambda num: num % 2 != 0

def main():
    num1= int(input("Enter a number: "))
    
    result= checkOdd(num1)

    if result:
        print("The number is Odd:", result)
    else:
        print("The number is Odd:", result)

if __name__ == "__main__":
    main()