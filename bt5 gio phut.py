# -*- coding: utf-8 -*-
"""
Created on Sun Aug 18 16:11:14 2024

@author: Student
"""

#Nhập vào thời gian theo định dạng dd:mm:
time_input = input("Nhập giờ, phút, giây theo định dạng :mm:")
dd, mm, yy = map(int, time_input.split(":"))
#Kiểm tra giờ phút giây có hợp lệ 
if 0<= dd < 24 and 0 <= mm < 60 and 0 <= yy < 60:
    #Đổi giò phút ra giây
    total_seconds = dd * 3600 + mm * 60 + yy
    
    #In kết quả ra màn hình
    print("Tổng số giây: Total seconds")
else:
    print("Giờ phút hoặc giây không hợp lệ")yy