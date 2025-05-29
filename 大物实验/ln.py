import math

while 1:
    number = float(input("Enter a number: "))
    ln = math.log(number)
    print("Natural logarithm of", number, "is", round(ln, 3))

    if input() == 'n':
        break
 