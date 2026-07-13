class Demo:
      value =21
      
      def __init__(self,no1,no2):
          self.value1= no1  
          self.value2= no2    

      def fun(self):
          print("value of no1",self.value1)
          print("value of no1",self.value2)       
      
      def gun(self):
          print("value of no1",self.value1)
          print("value of no1",self.value2) 

obj1 = Demo(11,21)
obj2 = Demo(23,101) 

obj1.fun()
obj2.fun()

obj1.gun()
obj2.gun()

