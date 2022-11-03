num1 = int(input("Enter a number: "))
if (0<=num1<=12):
    for num2 in range(0,13):
        print(num2, " x ", num1, "=", num1 * num2)
if (num1<0):
    for num2 in reversed(range (0,13)):
        print(num2, " x ", num1, "=", num1 * num2)