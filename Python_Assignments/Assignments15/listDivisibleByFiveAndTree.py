getListDivisibleBy5And3 =  lambda arr: list(filter(lambda x:x%5==0 and x%3==0, arr))

def main():
    size=0
    arr= list()
    print("enter the number of elemets")
    size= int(input())

    print("enter the elements")
    
    for i in range(size):
        arr.append(int(input()))

    result = getListDivisibleBy5And3(arr)

    print("List of numbers divisible by 5 and 3:", result)

    

if __name__ == "__main__":
    main()