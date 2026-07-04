checkOdd= lambda lstdata: list(filter(lambda x: x % 2 != 0, lstdata))

def main():
    size=0
    print("enter numbe rof elements")
    size= int(input())
    arr= list()
    for i in range(size):
        arr.append(int(input()))

    oddNumbers = checkOdd(arr)
    print(oddNumbers)

if __name__ == "__main__": 
    main()