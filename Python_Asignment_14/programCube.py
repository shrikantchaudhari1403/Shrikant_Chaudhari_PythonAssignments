cube = lambda x: x * x * x

def main():
    number = int(input("Enter a number: "))
    result= cube(number)
    print("The cube of the number is:", result)

if __name__ == "__main__":
    main()