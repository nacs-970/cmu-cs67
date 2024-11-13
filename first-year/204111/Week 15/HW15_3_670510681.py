#!/usr/bin/env python
# Atithep Thepkij
# 670510681
# HW15_3
# 204111 Sec 002
from math import sqrt,sin,cos
def count_segment(list_a: list[tuple[float]]) -> tuple[int]:
    # px, py, r
    q1,q2,q3,q4 = 0,0,0,0

    for circle in list_a:
        px,py,r = circle
        t1,t2,t3,t4 = False,False,False,False
        
        # right, left, top, bot, top right, top left, bot right, bot left
        # img: https://www.google.com/search?q=circle+trigonometry&sca_upv=1&udm=2#vhid=BTczvzSnSuBJzM&vssid=mosaic

        #circle_quardrant = set([(px+r, py), (px-r, py), (px, py+r), (px, py-r), \
        #                        (px+r / sqrt(2), py + r / sqrt(2)), (px-r / sqrt(2), py+r / sqrt(2)), (px+r / sqrt(2), py-r / sqrt(2)), (px-r / sqrt(2), py-r / sqrt(2)),])

        #circle_quardrant = set([(px+r,py), (sqrt(px+r)/2,sqrt(py+r)/2),\
        #                        (px,py+r), (-1 * sqrt(px+r)/2,sqrt(py+r)/2),\
        #                        (px+r,py+r), (-1 * sqrt(px+r)/2,-1 * sqrt(py+r)/2),\
        #                        (px-r,py), (px,py-r), (sqrt(px+r)/2,-1 * sqrt(py+r)/2)])

        #print(circle_quardrant)
        # for x,y in circle_quardrant:

        # https://www.youtube.com/watch?v=aHaFwnqH5CU
        # (x−h)^2 + (y−k)^2 = r^2
        # h,k is the center of the circle (origin).
        # x = r * cos(θ)
        # y = r * sin(θ)
        range_ = set(range(1,361,2))
        #print(range_)

        for radius in range_:
            x = px + (r * cos(radius))
            y = py + (r * sin(radius))

            if all([t1,t2,t3,t4]):
                break

            #print(x,y)
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
    return q1,q2,q3,q4
            #if (px + r) > 0 and (py + r) > 0:
            #    #print(circle,"q1")
            #    t1 = True
            ## - +
            #if (px - r) < 0 and (py + r) > 0:
            #    #print(circle,"q2")
            #    t2 = True
            ## - -
            #if (px - r) < 0 and (py - r) < 0:
            #    #print(circle,"q3")
            #    t3 = True
            ## + -
            #if (px + r) > 0 and (py - r) < 0:
            #    #print(circle,"q4")
            #    t4 = True


if __name__ == "__main__":
    assert count_segment([(2, 7, 1.5),(3.2, 2.5, 4.06),(-5.5, -4.5, 2.5),(2, -5.2, 3),(7.2, -2.8, 1.2)]) == (2,1,2,3)
