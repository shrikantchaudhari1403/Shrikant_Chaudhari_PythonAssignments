
filterEven= lambda lst: list(filter(lambda x: x%2==0 , lst))

def main():
    size=0;
    print("enter the number of elemets")
    size= int(input())
   
    arr= list()
    print("enter the elements")
    for i in range(size):
        arr.append(int(input()))

    even_numbers = filterEven(arr)
    print(even_numbers)

if __name__ == "__main__":
    main()