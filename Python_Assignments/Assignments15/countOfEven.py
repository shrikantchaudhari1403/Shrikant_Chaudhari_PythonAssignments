countofEven= lambda arr : len(list(filter(lambda x:x%2==0, arr)))


def main():
    size=0
    arr= list()
    print("enter the number of elemets")
    size= int(input())
    for i in range(size):
        arr.append(int(input()))
    
     
    result= countofEven(arr)
    print("Count of even numbers from the list:", result)

if __name__=="__main__":
    main()