#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW09_1
# 204111 Sec 002
def left_max(list_a:list[int]) -> list[int]:
    if list_a == []:
        return []
    return left_max(list_a[:len(list_a)-1]) + [max(list_a)]
if __name__ == '__main__':
    print(left_max([2,8,1]))
    print(left_max([3,3,1,1,2,4]))
    print(left_max([-3,-33,-101,-1,2,-10000]))
