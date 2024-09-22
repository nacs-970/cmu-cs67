#!/usr/bin/env python
# 670510681
# Atithep Thepkij (Tun)
# Lab13_1
# 204111 Sec 002

import random

def matrix_mult(m1:list[list[int]], m2:list[list[int]]) -> list[list[int]]:
    ans = []
    #min_,max_ = min(m1,m2),max(m2,m1)

    if len(m2) >= len(m1):
        min_ = m1; max_ = m2
    else:
        min_ = m2; max_ = m1

    transpose = list(zip(*max_))


    for i in range(len(min_)):
        temp = []
        for j in range(len(transpose)):

            if len(min_[i]) != len(transpose[j]):
                return None

            temp += [sum(list(map(lambda x,y: x*y,min_[i],transpose[j])))]
        ans += [temp]
    return ans

def test():
    for _ in range(9999):
        l1,l2 = [],[]

        len_ = random.randint(1,5)
        for _ in range(random.randint(1,10)):
            t = []
            for i in range(len_):
               t += [random.randint(1,100)]
            l1 += [t]

        len_ = random.randint(1,5)
        for _ in range(random.randint(1,10)):
            t = []
            for i in range(len_):
               t += [random.randint(1,100)]
            l2 += [t]
        if matrix_mult(l1,l2) == None:
            continue
        print(l1);print(l2)
        print("ans", matrix_mult(l1,l2))

if __name__ == "__main__":
    test()
    #print(matrix_mult([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]]))
    #print(matrix_mult([[1,2]],[[7,8],[9,10],[11,12]]))
    #print(matrix_mult([[1,2]],[[7,8],[9,10]]))
    #print(matrix_mult([[1,2,3],[4,5,6]],[[7,8,5,9,3],[9,10,-3,7,13],[11,12,6,2,9]]))

