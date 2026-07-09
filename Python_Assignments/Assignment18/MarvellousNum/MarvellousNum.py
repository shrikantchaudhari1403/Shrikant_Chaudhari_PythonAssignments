def CheckPrime(num):
    if num <=1:
       return False 
    
    factor=0
    for i in range(2,num):
        if num%i == 0:
          return False
          
    if factor > 2 :
       return False
    else:
       return True 
        


        