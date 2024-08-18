# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 14:34:28 2024

@author: Student
"""
 
a = float(input("Nhập hệ số a:"))
b = float(input("Nhập hệ số b:"))
c = float(input("Nhập hệ số c:"))

delta = b**2 - 4*a*c
if delta<0:
    print("Phương trình vô nghiệm")
elif delta==0:
    print("Phương trình có nghiệm kép")
    print("x1=x2=", -b/2*a )
else:
    print("Phương trình có hai nghiệm phân biệt")
          x1 = ((-b + math.sqrt(delta)) / (2 * a))
          x2 = ((-b - math.sqrt(delta)) / (2 * a))
    print("x1 =", x1)
    print("x2 =", x2)