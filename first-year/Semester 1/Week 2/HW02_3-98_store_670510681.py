#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW02_3
# 204111 Sec 002

x = float(input("Old price: "))
x = x - 50 # หาเลขหน้า
x = x // 100 # Confirm เลขหน้าหารไม่เอาเศษ
x = x * 100 # แปลงเลข
x += 98 # เพิ่ม 98

print(f"New Price: {int(x)}")