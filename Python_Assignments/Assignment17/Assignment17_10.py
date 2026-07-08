def additionDigits(no):
    result=0
    while no > 0:
          result=result + no % 10
          no= no // 10

    print(f"addition of total digits is {result}")


num= int(input("enter number: "))
additionDigits(num)
