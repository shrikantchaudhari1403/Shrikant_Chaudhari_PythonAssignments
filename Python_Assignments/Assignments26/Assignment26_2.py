class Circle:
     pii = 3.14

     def __init__(self):
          self.radius=0.0
          self.area=0.0
          self.curcumference=0.0

     def accept(self):
         num= float(input("enter the radius")) 
         self.radius=num

     def calculateArea(self):
         self.area= Circle.pii * self.radius ** 2
          
     def calculateCircumference(self):
         self.curcumference= 2*Circle.pii*self.radius

     def display(self):
         print("Radius: ",self.radius)     
         print("Area: ",self.area)     
         print("Curcumference: ",self.curcumference)      

cal1= Circle()

cal1.accept()
cal1.calculateArea()
cal1.calculateCircumference()
cal1.display()
