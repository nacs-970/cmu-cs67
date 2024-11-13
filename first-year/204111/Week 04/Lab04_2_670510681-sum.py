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
        max_ = a
        mid_ = b
    else:
        max_ = b
        mid_ = a
    if c>max_:
      max_=c
    else:
      mid_ = c
    min_ = (a+b+c) - max_ - mid_

    print(f"min = {min_}")
    print(f"mid = {mid}")
    print(f"max = {max_}")

if __name__ == "__main__":
    main()
