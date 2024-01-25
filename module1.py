#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Ученик
#
# Created:     25.01.2024
# Copyright:   (c) Ученик 2024
# Licence:     <your licence>

from math import*
def decorator(fonc):
    def rastoinie(V, V_0, t):
        a=fonc(V, V_0, t)
        print('Ускорение =',a)
        S = V_0*t+(a*pow(t,2))/2
        print('Растояние =',S)
    return rastoinie
def yscorenie(V, V_0, t):
    a=(V-V_0)/t
    return a

V=int(input("Введите скорость"))
V_0=int(input("Введите начальную скорость"))
t=int(input("Введите время"))

try:
    yscorenie=decorator(yscorenie)
    yscorenie(V,V_0,t)
except (ZeroDivisionError,ValueError):
    print('вводите числа и время не может быть равно нулю')
