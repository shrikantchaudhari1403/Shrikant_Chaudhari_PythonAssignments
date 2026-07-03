
maxNumber= lambda x, y: x if x > y else y

def main():
    numberFirst= int(input("Enter a first number: "))
    numberSecond= int(input("Enter a second number: "))
    result= maxNumber(numberFirst, numberSecond)
    print("The maximum number is:", result)
 

if __name__ == "__main__":
    main()  