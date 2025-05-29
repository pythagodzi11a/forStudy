import numpy as np
import math

data = [0]*5

for i in range(0,5):
    data[i] = float(input("Enter number: "))

# 平均数
avrange =  np.mean(data)
print(avrange,"\n")

# 标准偏差
Ssum = 0
for i in range(0,5):
    Ssum += pow(data[i]-avrange,2)
S = math.sqrt(Ssum/(len(data)-1))
print("标准偏差S(D): ",round(S,6),"\n")

# 坏值检测
print("坏值范围: [", round(avrange-3*S,5),",",round(avrange+3*S,5),"]\n")
for num in data:
    if(num<(avrange-3*S) or num>(avrange+3*S)):
        print("坏值: ",num,"\n")
        continue
    
# A类不确定度
tp = 1.14
miuA = S * tp / math.sqrt(len(data)) 
print("A类不确定度: ",round(miuA,5),"\n")

#B类不确定度
miuB = float(input("B类不确定度: "))

#总不确定度
miu = 2*math.sqrt(pow(miuA,2)+pow(miuB,2))
print("总不确定度为: ",miu,"\n")