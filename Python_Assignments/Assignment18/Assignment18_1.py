def listElementsAddition(num):
    total=0
    for i in num:
        total+= i
    return total



n= int(input("enter number of items in list: "))
data= []

print("enter elements 1 by 1: ")

for i in range(n):
    data.append(int(input()))


result=listElementsAddition(data)

print(f"addition of list elements is {result}")


    