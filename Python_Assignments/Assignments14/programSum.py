addition= lambda x,y: x+y

def main():
    num1= int(input("Enter a first number: "))
    second= int(input("Enter a second number: "))
    
    result= addition(num1, second)

    print("The sum of the two numbers is:", result)

if __name__ == "__main__":
    main()