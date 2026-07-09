import MarvellousNum

def returnList(numLst):
    listPrime =[]
    sumPrime=0
    for i in numLst:
        if MarvellousNum.CheckPrime(i) == True:
           listPrime.append(i) 
           sumPrime=sumPrime+i   
       
    return sumPrime


number= int(input("Enter number of iteam to create list: "))

listNumbers=[]
print("Enter number 1 by 1: ")

for i in range(number):
    listNumbers.append(int(input()))


primeSum= returnList(listNumbers)

print(f"sum of prime numbers from orinal list is {primeSum}")


