minNumber=lambda x, y: x if x < y else y

def main():
    num1= int(input("Enter a first number: "))
    num2= int(input("Enter a second number: "))
    result= minNumber(num1, num2)
    print("The minimum number is:", result)


if __name__ == "__main__":
    main()