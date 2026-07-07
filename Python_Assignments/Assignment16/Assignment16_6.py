def checkPositiveNegativeZero(num):
    if num > 0:
        print(num, "is a positive number.")
    elif num < 0:
        print(num, "is a negative number.")
    else:
        print(num, "is zero.")


num= int(input("Enter a number: "))
checkPositiveNegativeZero(num)        

