import Arithmetic


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result= Arithmetic.add(num1, num2)
print("Addition:", result)  

result= Arithmetic.subtract(num1, num2)
print("Subtraction:", result)   

result= Arithmetic.multiply(num1, num2)
print("Multiplication:", result)    

result= Arithmetic.devide(num1, num2)
print("Division:", result)      
