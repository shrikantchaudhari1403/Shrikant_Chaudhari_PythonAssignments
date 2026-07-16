class numbers:
    
      def __init__(self):
            num= int(input("Enter the number: "))
            self.value= num 
            

      def checkPrime(self):
          count= 0
          for i in range(2,self.value+1):
               if self.value % i ==0 :
                  count= count+1

          if count == 1:
             print("number is prime number")
          else:
               print("number is not prime number")
       

      def checkPerfect(self):
         sumVal = 0

         for i in range(1, self.value):
             if self.value % i == 0:
                sumVal += i

         if self.value == sumVal:
            print("number is perfect number")
         else:
            print("number is not perfect number") 
      
      def printFactors(self):
         factorArr=[]
       
         for i in range(1, self.value+1):
             if self.value % i == 0:
                factorArr.append(i)

         print("factors of the given numbers are :", factorArr )


      def printSumOfFactors(self):
         factorArr=[]
         sumFactors=0

         for i in range(1, self.value+1):
             if self.value % i == 0:
                factorArr.append(i)
                sumFactors+= i
       
         print("sum of factors of the given numbers are :", sumFactors )      


obj1=numbers()  

obj1.checkPerfect()
obj1.checkPrime()
obj1.printFactors()
obj1.printSumOfFactors()




                 


             

                 

                  