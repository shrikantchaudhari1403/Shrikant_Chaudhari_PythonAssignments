
from functools import reduce

findMin= lambda arr: reduce(lambda x,y : x if x < y else y,arr)

def main():
    size=0
    arr= list()
    print("enter the number of elemets")
    size= int(input())
    for i in range(size):
        arr.append(int(input()))
    
    result = findMin(arr)
    print("Minimum number from the list:", result)




if __name__ == "__main__":
    main()