#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab02_1
# 204111 Sec 002

import math
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
s = (a+b+c)/2
x = math.ceil((s*(s-a)*(s-b)*(s-c))**0.5)

print(f"area: {x}")
