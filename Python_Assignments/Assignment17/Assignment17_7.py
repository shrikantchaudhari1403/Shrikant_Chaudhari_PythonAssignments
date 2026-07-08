
def display(no):
    for i in range(1,no+1,1):
        for j in range(1,no+1,1):
            print(f"{j}", end=" ")

        print()

num = int(input("Enter a number: "))
display(num)        