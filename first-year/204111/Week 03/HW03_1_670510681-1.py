#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW03_1
# 204111 Sec 002
import math

def main():
    n = float(input())
    test_nearest_odd()
    print(f"{nearest_odd(n):.0f}")

def nearest_odd(n: float) -> float:
    # Odd number 2n+1 | 2m - 1 when n,m is int
    # 2n-1 ปัดขึ้น
    # Ex : 4.5/2 = 2.25 -> 3 ; 2(3)-1 = 5
    # Ex : -4.5/2 = -2.25 -> -2 ; 2(-2)-1 = -3
    # Ex : -4.5/2 = -2.25 -> -2 ; 2(-2)-1 = -3
    n = 2*(math.ceil(n/2))-1
    return int(n)

def test_nearest_odd() -> None:
    assert nearest_odd(-4.5) == -5
    assert nearest_odd(-5) == -5
    assert nearest_odd(3) == 3
    assert nearest_odd(3.9) == 3
    assert nearest_odd(3.5) == 3
    assert nearest_odd(4) == 3
    assert nearest_odd(4.5) == 5
    assert nearest_odd(2.12) == 3

    print("All OK!")

if __name__ == "__main__":
    main()
