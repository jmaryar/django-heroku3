#jr7yj
#Julia Rudy

import math

S = [1*10**6, 1.4*10**6, 0.5*10**6]
P = [.7,.9,.95]
Q = [0,0,0]
theta = [0,0,0]
RP = [0,0,0]
XP = [0,0,0]
XS = [0,0,0]
RS = [0,0,0]
Nominal_Voltage = 10*10**3


for i in range(len(S)):
    theta[i] = math.acos(P[i])
    P[i] = P[i]*S[i]
    Q[i] = math.sqrt(S[i]**2 - P[i]**2)
    RP[i] = (Nominal_Voltage**2)/P[i]
    XP[i] = (Nominal_Voltage**2)/Q[i]
    XS[i] = (RP[i]**2)/(XP[i]*((RP[i]/XP[i])**2+1))
    RS[i] = XS[i]*XP[i]/RP[i]

XPn

print(" ")
print("The Qs are " , Q)
print("The Ps are " , P)
print("The Ss are " , S)
print("The RPs are " , RP)
print("The XPs are " , XP)
print("The XSs are " , XS)
print("The RSs are " , RS)