#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW09_1
# 204111 Sec 002
def left_max(list_a:list[int]) -> list[int]:
    list_a = list(filter(lambda x: x>=0,list_a))
    if len(list_a) <= 1: return list_a
    if list_a[0] >= list_a[1]:
        list_a[1] = list_a[0]
        now = list_a[1]
        return [now] + left_max(list_a[1:])
    now = list_a[0]
    return [now] + left_max(list_a[1:])

def left_max2(list_a,n=1):
    if n == len(list_a):
        return list_a
    if list_a[n] < list_a[n-1]:
        list_a[n] = list_a[n-1]
    list_a = left_max2(list_a,n+1)
    return list_a

def test():
    import random
    for i in range(10000):
        l = []
        for i in range(1,random.randint(1,100)):
            l += [random.randint(0,100)]
        #print(l)
        try:
            assert left_max2(l) == left_max(l)
        except:
            print('expect:',left_max(l))
            print('got   :',left_max2(l))
            return 0
    print(';-;')
if __name__ == '__main__':
    print(left_max([2,8,1]))
    print(left_max([-1,8,1]))
    print(left_max([3,3,1,1,2,4]))
    test()
