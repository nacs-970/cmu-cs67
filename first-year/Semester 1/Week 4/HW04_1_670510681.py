#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW04_1
# 204111 Sec 002

def main():
    #test()
    p = int(input())
    c = int(input())
    print(calculate_exp(p,c))

def calculate_exp(p: int, c: int) -> int:
    evoc = 2*(c//12) + 2*((p-1)//12)
    return evoc
    
    #print((c+(c//12)+(p-(c//12)))//12)

def test():
    assert calculate_exp(1,12) == 1000
    assert calculate_exp(24,0) == 2000
    assert calculate_exp(24,24) == 4000
    assert calculate_exp(13,0) == 1000
    assert calculate_exp(2,12) == 1000
    assert calculate_exp(2,22) == 2000

if __name__ == "__main__":
    main()
