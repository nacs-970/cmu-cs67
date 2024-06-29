#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW03_1
# 204111 Sec 002

def nearest_odd(n):
    # Odd number 2n+1 | 2m - 1 when n,m is int

    # ex:
    # 3 : 3-0.5 = 2.5
    # 2 // 2 = 1
    # (2*1)+1 = 3

    # 4 : 4-0.5 = 3.5
    # 3.5 // 2 = 1
    # (2*1)+1 = 3

    # 4.5 : 4.5-0.5 = 4
    # 4 // 2 = 2
    # (2*2)+1 = 5

    # 6.5 : 6.5-0.5 = 6
    # 6 // 2 = 3
    # (2*3)+1 = 7

    n = 2*((n-0.5)//2)+1
    return f"{n:.0f}"

n = float(input())

if __name__ == "__main__":
    print(nearest_odd(n))
