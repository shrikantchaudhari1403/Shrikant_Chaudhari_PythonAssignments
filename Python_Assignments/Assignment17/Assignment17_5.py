def checkPrime(num):
    isPrime= True
    if num<=1:
        print(f"{num} is not a prime number.")
        isPrime= False
    else:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                isPrime= False
                break

    if isPrime==True:
        print(f"{num} is a prime number.")


num = int(input("Enter a number: "))
checkPrime(num)        