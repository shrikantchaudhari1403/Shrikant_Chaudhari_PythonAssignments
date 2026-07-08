def countDigits(no):
    count=0
    while no > 0:
          count= count+1
          no= no // 10
          
          
    print(f"total number's are {count}") 
  
num= int(input("enter no "))
countDigits(num)

