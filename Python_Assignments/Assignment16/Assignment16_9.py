def display(no):
    startNum=1
    while no >= 1:
          startNum= startNum + 1
          if startNum % 2 == 0:
              print(startNum)
              no= no - 1

                
num= int(input("Enter number of even numbers to print: "))
display(num)