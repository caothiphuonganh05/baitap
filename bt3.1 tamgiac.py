# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:24:00 2024

@author: Student
"""

a = float(input("Nhập hệ số a: "))
b = float(input("Nhập hệ số b: "))
c = float(input("Nhập hệ số c: "))
if a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a):
    print("a, b, c là cạnh của một tam giác.")
else:
    print("a,b,c không là cạnh của một tam giác.")