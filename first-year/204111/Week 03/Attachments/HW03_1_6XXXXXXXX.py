#!/usr/bin/env python3
# ชื่อ นามสกุล (ชื่อเล่น)
# 6XXXXXXXX
# HW03_1
# 204111 Sec 00B

def main():
    test_nearest_odd()


# implement ฟังก์ชันนี้ให้ถูกต้อง
def  nearest_odd(x: float) -> int:
    return 0


# เพิ่ม test case อื่นๆ ตามความเหมาะสม
def test_nearest_odd() -> None:
    assert nearest_odd(3) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    print("All OK!")


if __name__ == '__main__':
    main()