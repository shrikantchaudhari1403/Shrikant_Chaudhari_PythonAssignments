returnLargest=lambda x,y,z: max(x,y,z)


def main():
    num1= int(input("Enter a first number: "))
    num2= int(input("Enter a second number: "))
    num3= int(input("Enter a third number: "))
    result= returnLargest(num1, num2, num3)
    print("The largest number is:", result)

if __name__ == "__main__":
    main()