#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab04_1
# 204111 Sec 002

import math

def main():
    test_circle_intersect()
    x1 = float(input())
    y1 = float(input())
    r1 = float(input())
    x2 = float(input())
    y2 = float(input())
    r2 = float(input())
    circle_intersect(x1,y1,r1,x2,y2,r2)

# d = เส้น จุดศูนย์กลาง 2 วง
# เมื่อ d - (r1+r2) <= epsilon วงทบกัน
# เมื่อ d - (r1+r2) > 0  วงห่างกัน
# เมื่อ d - (r1+r2) < 0  วงทับกัน
def circle_intersect(x1:float,y1:float,r1:float,
                     x2:float,y2:float,r2:float,
                     epsilon=10**-6) ->int:
    d = (((x1-x2)**2)+((y1-y2)**2))**0.5
    
    # เทียบ d กับ r1+r2 ที่ค่าไม่มากกว่า epsilon
    if math.isclose(r1+r2,d,abs_tol = epsilon) == True:
        return 0
    else:
        if  d-(r1+r2)>0:
            return -1
        else:
            return 1
def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("all ok!")

if __name__ == "__main__":
    main()
