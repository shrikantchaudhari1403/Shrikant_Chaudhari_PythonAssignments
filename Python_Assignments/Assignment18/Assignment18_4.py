def checkFrequencyFromList(lst,no):
    count=0
    for i in lst:
        if no==i:
           count=count+1
          
    return count          


n=int(input("Enter number of elements in list: "))

print("enter elements 1 by 1: ")
listData=[]

for i in range(n):
    listData.append(int(input()))

number= int(input("enter number to check frequency :"))

frequency= checkFrequencyFromList(listData,number)

print(f"friquenct of number : {number}: in list {listData} is {frequency}")

