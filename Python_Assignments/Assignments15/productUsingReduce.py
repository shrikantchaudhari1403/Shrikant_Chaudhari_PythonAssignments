from functools import reduce


reducrProduct=lambda arr: reduce(lambda x,y: x*y, arr)

def main():
    size=0
    arr= list()
    print("enter the number of elemets")
    size= int(input())
    print("enter the elements")
    for i in range(size):
        arr.append(int(input()))

    result=reducrProduct(arr)
    print("Product of all elements:", result)
   
if __name__=="__main__":
    main()