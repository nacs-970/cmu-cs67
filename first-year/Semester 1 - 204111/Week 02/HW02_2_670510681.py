#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW02_2
# 204111 Sec 002

x = int(input("x: "))-1 # ex: 3 ถึง 3 ให้เอา 3*3 ไม่เอา ชั้นอื่นๆ  รวมชั้น 3 - รวมชั้น 2 = แค่ ชั้น 3
y = int(input("y: "))
# เลือก 5-8 เอาชั้น 8,7,6,5 เท่ากับ sum(8)^2 - sum(5-1)^2

# Summation i^2 (n*(n+1)*(2*(n+1)))/6
sumy = (y*(y+1)*(2*y+1))/6
sumx = (x*(x+1)*(2*x+1))/6 

print(f"sum is: {sumy-sumx:.0f}")