def display(no):
    for i in range(no,0,-1):
        for j in range(i):
            print("*", end=" ")

        print()

num = int(input("Enter a number: "))
display(num)        