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
    min,max = a,a
    if b<min:
        min=b
    if c<min:
        min=c

    if b>max:
        max=b
    if c>max:
        max=c

    mid = (a+b+c)-min-max

    print(f"min = {min}")
    print(f"mid = {mid}")
    print(f"max = {max}")

if __name__ == "__main__":
    main()
