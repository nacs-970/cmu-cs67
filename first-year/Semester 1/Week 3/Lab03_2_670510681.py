#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab03_2
# 204111 Sec 002

# AB = x, AC = 2x,BC = ?
# c^2 = a^2 + b^2
# c^2 = x^2 + (2x)^2
# c = (5x^2)^0.5 = sqrt(5)x

def rectangle_area(x:float) -> float:
    ab = x
    ac = 2*x
    bc = (5**0.5)*x
    s = (2*bc)/7
    s = s**2
    return s

def main():
    x = float(input())
    print(f"{rectangle_area(x):.2f}")

if __name__ == "__main__":
    main()
