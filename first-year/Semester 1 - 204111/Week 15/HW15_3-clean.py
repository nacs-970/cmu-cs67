#!/usr/bin/env python
# Atithep Thepkij
# 670510681
# HW15_3
# 204111 Sec 002
# TA Film & Kla for explanation

from math import sqrt
def count_segment(list_a: list[tuple[float]]) -> tuple[int]:
    # px, py, r
    q1,q2,q3,q4 = 0,0,0,0

    for circle in list_a:
        px,py,r = circle
        t1,t2,t3,t4 = False,False,False,False
        # diagonal becase if zero_radius is more than radius mean across quadrant
        zero_radius = sqrt((px**2) + (py**2))

        # + +
        if px > 0 and py > 0:
            t1 = True
            if px - r < 0:
                t2 = True
            if py - r < 0:
                t4 = True
            if zero_radius < r:
                t3 = True

        # - +
        elif px < 0 and py > 0:
            t2 = True
            if px + r > 0:
                t1 = True
            if py - r < 0:
                t3 = True
            if zero_radius < r:
                t4 = True

        # - -
        elif px < 0 and py < 0:
            t3 = True
            if px + r > 0:
                t4 = True
            if py + r > 0:
                t2 = True
            if zero_radius < r:
                t1 = True

        # + -
        elif px > 0 and py < 0:
            t4 = True
            if px - r < 0:
                t3 = True
            if py + r > 0:
                t1 = True
            if zero_radius < r:
                t2 = True

        # - .
        elif px < 0 and py == 0:
            if py + r > 0:
                t2 = True
            if py - r < 0:
                t3 = True
            if zero_radius < r:
                t1,t4 = True,True

        # + .
        elif px > 0 and py == 0:
            if py + r > 0:
                t1 = True
            if py - r < 0:
                t4 = True
            if zero_radius < r:
                t2,t3 = True,True

        # . -
        elif px == 0 and py < 0:
            if px + r > 0:
                t4 = True 
            if px - r < 0:
                t3 = True
            if zero_radius < r:
                t1,t2 = True,True
        # . +
        elif px == 0 and py > 0:
            if px + r > 0:
                t1 = True 
            if px - r < 0:
                t2 = True
            if zero_radius < r:
                t3,t4 = True,True

        else:
            t1,t2,t3,t4 = True,True,True,True

        #print(circle, zero_radius, t1,t2,t3,t4)

        if t1: q1 += 1
        if t2: q2 += 1
        if t3: q3 += 1
        if t4: q4 += 1

    #print(q1,q2,q3,q4)
    return q1,q2,q3,q4

if __name__ == "__main__":
    assert count_segment([(2, 7, 1.5),(3.2, 2.5, 4.06),(-5.5, -4.5, 2.5),(2, -5.2, 3),(7.2, -2.8, 1.2)]) == (2,1,2,3)
    #count_segment([(3.2, 2.5, 4.06)])
    count_segment([(0,0,1)])
    count_segment([(0,1,1)])
    count_segment([(0,1,2)])
    #count_segment([(0,0,1),(0,0,2)])
    #count_segment([(2,0,2)])
