def checkMaxFRomList(lst):
    maxNum= lst[0]
    for i in lst:
        if i > maxNum:
           maxNum=i 

    return maxNum

n=int(input("Enter number of elements in list: "))

print("enter elements 1 by 1: ")
listData=[]

for i in range(n):
    listData.append(int(input()))

result= checkMaxFRomList(listData)

print(f"maximum number in the list:  {result} ")

