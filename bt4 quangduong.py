# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 15:51:01 2024

@author: Student
"""
discout=92/100 
a=float(input("Số km quãng đường đi được."))
if a<=1:
    st=20.000
    print("số tiền",st)
elif a<=3:
    st=a*13.000
    print("số tiền",st)
elif 4<=a<=8:
    st=a*13.000 + (a-3)*12.000
    print("số tiền",st)
elif a>8:
    st=a*13.000 + (a-3)*10.000
    print("số tiền",st)
    if st > 100.000:
        TT =st*discout
        print("Tổng số tiền",tt)
