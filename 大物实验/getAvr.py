while 1:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    avr = (num1 + num2) / 2
    print("Average of", num1, "and", num2, "is", round(avr,5))
    ch = input("Do you want to continue? (y/n): ")
    if ch == 'n':
        break
