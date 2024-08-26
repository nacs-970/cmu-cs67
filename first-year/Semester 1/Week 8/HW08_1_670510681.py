#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW08_1
# 204111 Sec 002

from math import isclose

#def pi(n:int) -> float:
#    if n <= 0:return 0
#    now = 4/(n+2)
#    next = pi(n-1)
#    return 4 - now + next

def pi(n: int) -> float:
    # Wiki Rate of convergence from : https://en.wikipedia.org/wiki/Pi
    def find_remainder(n):
        if n <= 0:return 0
        x = n*2
        now = 4/((x)*(x+1)*(x+2))
        next_ = find_remainder(n-1)
        
        # 3 + (now - next) -> per + (now1 - next1)
        #print(now)
        #print(next)
        remainder = now - next_
        #print(remainder,now,next)
        return remainder

    return 3 + abs(find_remainder(n))

def test_pi():
    epsilon = 10**-10
    assert isclose(pi(0), 3, abs_tol=epsilon)
    assert isclose(pi(1), 3.1666666666666665, abs_tol=epsilon)
    assert isclose(pi(2), 3.1333333333333333, abs_tol=epsilon)
    assert isclose(pi(5), 3.1427128427128426, abs_tol=epsilon)
    print("All OK!")

if __name__ == "__main__":
    print(pi(0))
    #print(pi(1))
    print(pi(2))
    #print(pi(3))
    #print(pi(4))
    print(pi(5))
