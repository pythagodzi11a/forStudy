import math

UL = [0]*10
UC = [0]*10
UR = [0]*10
US = [0]*10
# 读取数据

for i in range(0,10):
    UL[i] = float(input("Enter UL: "))
for i in range(0,10):
    UR[i] = float(input("Enter UR: "))
for i in range(0,10):
    UC[i] = float(input("Enter UC: "))

for i in range (0,10):
    US[i] = math.sqrt(UR[i]**2+(UL[i]-UC[i])**2)

VS_Avr = sum(US)/10

for i in range (0,10):
    print("US: ", US[i])

print ("VS_Avr: ", VS_Avr)
