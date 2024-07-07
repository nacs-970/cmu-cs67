#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab04_2
# 204111 Sec 002


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    my_min_mid_max(a,b,c)

def my_min_mid_max(a:int,b:int,c:int) -> None:
    if a > b:
        max = a
        mid = b
    else:
        max = b
        mid = a

    if c > max:
        if max == a:
            max = c
            mid = a
            min = b
        else:
            max = c
            mid = b
            min = a
    else:
        if c > mid:
            if max == a:
                max = a
                mid = c
                min = b
            else: 
                max = b
                mid = c
                min = a
        else:
            if max == a:
                max = a
                mid = b
                min = c
            else: 
                max = b
                mid = a
                min = c

    print(f"min = {min}")
    print(f"mid = {mid}")
    print(f"max = {max}")

if __name__ == "__main__":
    main()
