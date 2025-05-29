import math

B = [0]*10
fi = [0]*10

A = float(input("Enter A: "))

for i in range(0,10):
    B[i] = float(input("Enter B: "))

for i in range (0,10):
    fi[i] = math.asin(B[i]/A)

for i in range (0,10):
    print("fi: ", fi[i])
