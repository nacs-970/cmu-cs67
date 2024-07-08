#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW04_1
# 204111 Sec 002

def main():
    test()
    p = int(input())
    c = int(input())
    print(calculate_exp(p,c))

def calculate_exp(p: int, c: int) -> int:
    if p > 0:
        # find max evolve
        total = p+c
        # pidgy = candy
        # เมื่อ evolve ครั้งแรก จะใช้ 13ก้อนเสมอ หลังจากนั้นจะเป็นการลบ 11 ต่อครั้ง จนกว่าจะไม่สามารถลบได้อีก, +1 เพราะครั้งแรกไม่ได้นับ
        # first evolve allway using 13 candy after that subtract by 11 untill no more to subtract, +1 for first evolve
        max_evolve = ((total-13)//11) + 1
        # if base pidgy is <= หมายความว่า จะไม่มีการ evolve ไปมากกว่า จน. pidgy
        if p <= max_evolve:
            return p*1000
        # if base pidgy is > max_evolve หมายความว่าจะ evolve ไม่สูงไปกว่า max_evolve แม้จะมี p มากแค่ไหนก็ตาม
        else:
            return max_evolve*1000
    else:
        return 0

def test():
    assert calculate_exp(20,1) == 1000
    assert calculate_exp(20,11) == 2000
    assert calculate_exp(1,12) == 1000
    assert calculate_exp(11,12) == 1000
    assert calculate_exp(24,0) == 2000
    assert calculate_exp(13,0) == 1000
    assert calculate_exp(2,12) == 1000
    assert calculate_exp(2,22) == 2000
    assert calculate_exp(120,0) == 10000
    assert calculate_exp(6,62) == 6000
    assert calculate_exp(6,61) == 5000
    assert calculate_exp(1200,0) == 108000
    print(":)")
if __name__ == "__main__":
    main()
