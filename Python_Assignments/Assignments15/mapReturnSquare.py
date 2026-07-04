
getSquare = lambda x: x * x

def main():
    size=0
    arr= list()
    print("enter the number of elemets")
    size= int(input())

    print("enter the elements")
    for i in range(size):
        arr.append(int(input()))

    squared_numbers = list(map(getSquare,arr))

    print(squared_numbers)

if __name__ == "__main__":
    main()