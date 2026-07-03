checkDivisibleByFive= lambda x: True if x % 5 == 0 else False


def main():
    number= int(input("Enter Number: "))
    result = checkDivisibleByFive(number)

    if result:
        print("The number is divisible by 5: ", result)
    else:
        print("The number is divisible by 5: ", result)


if __name__ == "__main__":
    main()