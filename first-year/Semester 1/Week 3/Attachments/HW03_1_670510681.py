#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW03_1
# 204111 Sec 002

def main():
    test_nearest_odd()

# implement ฟังก์ชันนี้ให้ถูกต้อง
def  nearest_odd(x: float) -> int:
    x = 2*((x-0.5)//2)+1
    return int(x)

# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_nearest_odd() -> None:
    assert nearest_odd(3) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    print("All OK!")

if __name__ == '__main__':
    main()
