class BookStore:
      noOfBooks=0

      def __init__(self, name, author):
            BookStore.noOfBooks+=1

            self.bookNo= BookStore.noOfBooks
            self.value1= name
            self.value2= author
   
      def display(self):
          print(f"{self.value1} by {self.value2} no of books: {self.bookNo}")


obj1= BookStore("Life of PI","Shrikant")           
obj2= BookStore("Tiger jonda hai","Boman Irani") 

obj1.display()
obj2.display()