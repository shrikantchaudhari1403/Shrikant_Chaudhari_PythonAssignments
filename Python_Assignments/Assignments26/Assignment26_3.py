class Arithmetic:
      
      def __init__(self):
            self.value1= 0
            self.value2= 0

      def accept(self):
          self.value1= int(input("enter value1"))
          self.value2= int(input("enter value2"))
      
      def addition(self):
          return self.value1+self.value2 
      
      def substraction(self):
          return self.value1-self.value2 
      
      def multiplecation(self):
          return self.value1*self.value2 
      
      def division(self):
          return self.value1/self.value2
      

ob1= Arithmetic()

ob1.accept()

print("Addition =", ob1.addition())
print("Subtraction =", ob1.substraction())
print("Multiplication =", ob1.multiplecation())
print("Division =", ob1.division())
