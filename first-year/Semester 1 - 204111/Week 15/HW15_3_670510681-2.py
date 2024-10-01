#!/usr/bin/env python
# Atithep Thepkij
# 670510681
# HW15_3
# 204111 Sec 002
from math import sqrt,sin,cos
from time import time
def count_segment(list_a: list[tuple[float]]) -> tuple[int]:
    # px, py, r
    start = time()
    q1,q2,q3,q4 = 0,0,0,0
    range_ = set(range(0,360,45))
    #print(range_)
    
    #print(range_)
    #list_ = set(list_a)

    for circle in list_a:
        px,py,r = circle
        t1,t2,t3,t4 = False,False,False,False

        # https://www.youtube.com/watch?v=aHaFwnqH5CU
        # Polar coordinates, Cartesian coordinates
        # (x−h)^2 + (y−k)^2 = r^2
        # h,k is the center of the circle (origin).
        # x = r * cos(θ)
        # y = r * sin(θ)
        
        for radius in range_:

            if all([t1,t2,t3,t4]):
                break

            x = px + (r * cos(radius))
            y = py + (r * sin(radius))
            
            # + +
            if x > 0 and y > 0:
                #print(circle,"q1")
                t1 = True
            # - +
            if x < 0 and y > 0:
                #print(circle,"q2")
                t2 = True
            # - -
            if x < 0 and y < 0:
                #print(circle,"q3")
                t3 = True
            # + -
            if x > 0 and y < 0:
                #print(circle,"q4")
                t4 = True

        if t1: q1 += 1
        if t2: q2 += 1
        if t3: q3 += 1
        if t4: q4 += 1

    #print(q1,q2,q3,q4)
    #print(f"{time() - start:.010f}")
    return q1,q2,q3,q4

if __name__ == "__main__":
    assert count_segment([(2, 7, 1.5),(3.2, 2.5, 4.06),(-5.5, -4.5, 2.5),(2, -5.2, 3),(7.2, -2.8, 1.2)]) == (2,1,2,3)
    print(count_segment([(0,0,1), (1,1,1), (-1,1,1), (-1,-1,1), (1,-1,1)]))
    print(count_segment([(-1,1,1)]))
