#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Sec 002

def is_right_triangle(a, b, c):
    max_ = max(a,b,c)
    min_ = min(a,b,c)
    mid = (a+b+c) - max_ - min_
    if min_**2 + mid**2 == max_**2:return True
    return False

if __name__ == '__main__':
    assert is_right_triangle(3, 4, 5) is True
    assert is_right_triangle(4, 3, 5) is True
    print("All OK!")
