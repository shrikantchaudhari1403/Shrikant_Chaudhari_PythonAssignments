
from functools import reduce

reduceNumber= lambda nums: reduce(lambda x,y : x+y,nums)

def main():
    size=0
    arr= list()
    print("enter the number of elements")
    size= int(input())
    
    for i in range(size):
        arr.append(int(input()))
        
    result = reduceNumber(arr)
    print("Sum of all elements:", result)
    



if __name__ == "__main__":
    main()