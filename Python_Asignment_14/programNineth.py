multiplication= lambda x,y: x*y

def main():
    num1= int(input("Enter a first number: "))
    second= int(input("Enter a second number: "))
    result= multiplication(num1, second)
    print("The product of the two numbers is:", result)

if __name__ == "__main__":
    main()