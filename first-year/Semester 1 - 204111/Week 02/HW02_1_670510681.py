#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW02_1
# 204111 Sec 002

m1 = float(input('m1: '))
b1 = float(input('b1: '))
m2 = float(input('m2: '))
b2 = float(input('b2: '))
# สมการ y = m(x)+b
# หา x โดยเอาสมการมาเท่ากับ y1 = y2
m = m1 - m2
b = b2 - b1
x = b/m
# แทน x
y = (m1*x)+b1

print(f'Lines intersect at ({x:.2f},{y:.2f})')
