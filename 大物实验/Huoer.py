import math

U1_1 = {"1.5": -4.40 , "2.0": -5.88 , "2.5": -7.36 , "3.0": -8.83 , "3.5":-10.30}
U1_2 = {"1.5":  1.53 , "2.0":  2.05 , "2.5":  2.55 , "3.0":  3.05 , "3.5":  3.54}
U1_3 = {"1.5": -1.53 , "2.0": -2.05 , "2.5": -2.55 , "3.0": -3.06 , "3.5": -3.56}
U1_4 = {"1.5":  4.40 , "2.0":  5.87 , "2.5":  7.36 , "3.0":  8.79 , "3.5": 10.27}

U2_1 = {"100": -4.75 , "200": -6.14 , "300": -7.52 , "400": -8.92 , "500":-10.30}
U2_2 = {"100": -1.98 , "200": -0.61 , "300": -0.76 , "400":  2.15 , "500":  3.53}
U2_3 = {"100":  1.97 , "200":  0.59 , "300": -0.78 , "400": -2.17 , "500": -3.55}
U2_4 = {"100":  4.74 , "200":  6.11 , "300":  7.49 , "400":  8.88 , "500": 10.26}

U1_H = {"1.5":  0.00 , "2.0":  0.00 , "2.5":  0.00 , "3.0":  0.00 , "3.5":  0.00}
U2_H = {"100":  0.00 , "200":  0.00 , "300":  0.00 , "400":  0.00 , "500":  0.00}

def cal_UH (U_1, U_2, U_3, U_4,U_H):
    result = 0.0
    for i in U_H:
        U_H[i] = (abs(U_1[i]) + abs(U_2[i]) + abs(U_3[i]) + abs(U_4[i])) / 4.0



cal_UH(U2_1, U2_2, U2_3, U2_4,U2_H)
for i in U2_H:
     print("U_H: ", round(U2_H[i],2))
# def cal_UH_and_IS (U1_1, U1_2, U1_3, U1_4,U_H):
#     result = 0.0
#     for i in U_H:
#         U_H[i] = (abs(U1_1[i]) + abs(U1_2[i]) + abs(U1_3[i]) + abs(U1_4[i])) / 4.0

#     for i in U_H:
#         print("U_H: ", round(U_H[i],2))
#     for i in U_H:
#         result += float(i)
#     IS = result / 5.0
#     UH = sum(U_H.values()) / 5.0

#     return round(UH,3), round(IS,2)

# B = [0]*20
# def cal_B (U,final):
#     for i in range(0, 20):
#         final[i] = U[i] / 5.0

# for i in U1_H:
#     U1_H[i] = (abs(U1_1[i]) + abs(U1_2[i]) + abs(U1_3[i]) + abs(U1_4[i])) / 4.0

# for i in U1_H:
#     print("U1_H: ", round(U1_H[i],4))

# result = 0.0
# for i in U1_H:
#     result += float(i)
# IS = result / 5.0
# UH = sum(U1_H.values()) / 5.0

# UH1 , IS1  = cal_UH_and_IS(U2_1, U2_2, U2_3, U2_4,U2_H)
# UH2 , IS2  = cal_UH_and_IS(U2_1, U2_2, U2_3, U2_4,U2_H)

# print("IS1: ", IS2)
# print("UH1: ", UH2)
# print("Finish cal IS1 and UH1")

# result = 0.0
# for i in U1_H:
#     result += float(i) * U1_H[i]
# xy_avr = result / 5.0
# print("xy_avr: ", xy_avr)

# x_avr_y_avr1 = IS2*UH2
# y_avr_squre1 = UH2**2
# print("x_avr_y_avr: ", x_avr_y_avr1)
# print("y_avr_squre: ", y_avr_squre1)

# result = 0.0
# for i in U1_H:
#     result += U1_H[i]**2
# y_squre_avr1 = result / 5.0
# print("y_squre_avr: ", y_squre_avr1)

# result = 0.0
# for i in U1_H:
#     result += float(i)**2
# x_squre_avr1 = result / 5.0

# x_avr_squre1 = 2.50**2
# print("x_avr_squre: ", x_avr_squre1)
# print("x_squre_avr: ", x_squre_avr1)


# print("test: ",(x_squre_avr1 - x_avr_squre1) * (y_squre_avr1 - y_avr_squre1))
# r = (xy_avr - x_avr_y_avr1) / math.sqrt((x_squre_avr1 - x_avr_squre1) * (y_squre_avr1 - y_avr_squre1))
# print("r: ", r)

# a1 = (xy_avr - x_avr_y_avr1) / (x_squre_avr1 - x_avr_squre1)
# a0 = UH2 - a1 * IS2
# print("y = ", round(a1,3) , "x + ", a0)
