#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab09_2
# 204111 Sec 002
def life_path(n:int) -> int:
    if len(str(n)) == 1:return n
    next_ = n%10 + life_path(n//10)

    if len(str(next_)) == 1:return next_
    return  next_%10 + life_path(next_//10)
if __name__ == '__main__':
    print(life_path(13092004))
    print(life_path(35))
    print(life_path(7))
