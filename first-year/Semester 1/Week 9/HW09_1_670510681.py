#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW09_1
# 204111 Sec 002
def left_max(list_a:list[int]) -> list[int]:
    list_a = list(filter(lambda x: x>=0,list_a))
    if len(list_a) == 1: return list_a
    if list_a[0] >= list_a[1]:
        list_a[1] = list_a[0]
        now = list_a[1]
        return [now] + left_max(list_a[1:])
    now = list_a[0]
    return [now] + left_max(list_a[1:])
if __name__ == '__main__':
    print(left_max([2,8,1]))
    print(left_max([-1,8,1]))
    print(left_max([3,3,1,1,2,4]))
