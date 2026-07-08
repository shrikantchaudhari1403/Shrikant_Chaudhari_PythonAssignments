def factorAddition(num):
    result = 0
    while num >= 1:
        result += num
        num -= 1
    return result


num = int(input("Enter a number: "))
result = factorAddition(num)
print(f"The sum of the first {num} natural numbers is: {result}")