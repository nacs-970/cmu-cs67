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
        min = b
    else:
        max = b
        min = a

    if c < min:
        mid = min
        min = c
    else:
        mid = c

    if c > max:
        mid = max
        max = c
    else:
        mid = c

    print(f"min = {min}")
    print(f"mid = {mid}")
    print(f"max = {max}")

if __name__ == "__main__":
    main()
