class BankAccount:
      roi= 10.5

      def __init__(self, name, amount):
            self.value1= name
            self.value2= amount
            

      def display(self):
          print(f"{self.value1} current balance : {self.value2}")

      def deposit(self, amount):
          self.value2= self.value2 + amount

      def withdral(self, amount):
          if self.value2 > 0 :
             self.value2= self.value2- amount


      def calculateInterest(self):
           return self.value2 * BankAccount.roi/100



obj1=BankAccount("shrikant",2000)  

obj2=BankAccount("jyoti",3000)   


obj1.display()

obj1.deposit(100)
obj1.withdral(200)
obj1.calculateInterest()

obj2.deposit(300)
obj2.withdral(100)
print(f"{obj1.calculateInterest()}")


obj1.display()
obj2.display()
print(f"{obj2.calculateInterest()}")










                        