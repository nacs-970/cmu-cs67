#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab03_1
# 204111 Sec 002

# r = 4*pi*r^2
# area = 4/3*pi*r^3
# r(surface) == r(area)

from math import pi as pi

def find_r_from_surface_area(area):
    r = (area/(4*pi))**0.5
    return r

def sphere_volume(r):
    area = (4/3)*pi*(r**3)
    return area

area = float(input("input surface area: "))
r = find_r_from_surface_area(area)

if __name__ == "__main__":
    print(f"volume = {sphere_volume(r):.2f}")
