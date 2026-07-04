from functools import reduce

getGreaterThanfiveCharaters = lambda lst: list(filter(lambda x: len(x) > 5, lst))

def main():
    size=0
    arr=list()
    print("enter the number of elemets")
    size= int(input())  
    for i in range(size):
        arr.append(input())

    result = getGreaterThanfiveCharaters(arr)
    print("String with more than five characters:", result)


if __name__== "__main__":
    main()