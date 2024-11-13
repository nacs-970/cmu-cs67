#!/usr/bin/env python3
# ชื่อ นามสกุล (ชื่อเล่น)
# 6XXXXXXXX
# Lab03_1
# 204111 Sec 00B

import math


def main():
    # รับข้อมูลพื้นที่ผิวจาก user
    surface_area = float(input("input surface area: "))

    # นำพื้นที่ผิวที่ได้มาคำนวณหารัศมี
    radius = find_r_from_surface_area(surface_area)

    # นำรัศมีที่คำนวณได้มาคำนวณหาปริมาตร
    volume = sphere_volume(radius)

    # แสดงปริมาตรทรงกลม แบบทศนิยมสองต่ำแหน่ง
    print(f"volume = {volume:.2f}")



def find_r_from_surface_area(surface_area: float) -> float:
    return 0


def sphere_volume(radius: float) -> float:
    return 0


if __name__ == '__main__':
    main()
