def display(no):
    for i in range(1,no+1):
        for j in range(1,i+1):
            print(j,end=" ")

        print()


num = int(input("Enter a number: "))
display(num)                    