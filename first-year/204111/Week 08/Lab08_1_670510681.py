#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab08_1
# 204111 Sec 002

def gcd(x:int,y:int) -> int:
    x,y = abs(x),abs(y)
    x,y = max(x,y),min(x,y) # find min max
    #if x < y: x,y = y,x # find min max
    if x % y == 0: return y
    reminder = x % y
    return gcd(y,reminder)

if __name__ == "__main__":
    print(gcd(19,71))
    print(gcd(71,19))
    print(gcd(99,11))
    print(gcd(-39,78))
