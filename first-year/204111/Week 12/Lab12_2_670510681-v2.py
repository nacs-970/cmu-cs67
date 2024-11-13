#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# Lab12_2
# 204111 Sec 002

def multiply_polynomials(p1: list[int], p2: list[int]) -> list[int]:
    # start from behind [2,0,3] -> 2x^2 + 0x^1 + 3x^0

    # insert power | power, coeff
    p1wp = list(map(lambda x,y: [x,y],range(len(p1)),p1[::-1]))
    p2wp = list(map(lambda x,y: [x,y],range(len(p2)),p2[::-1]))

    max_,min_ = max(p1wp,p2wp),min(p1wp,p2wp)

    dict_ = {}
    for x in max_:
        for y in min_:
            dict_[x[0]+y[0]] = dict_.get(x[0]+y[0],0) + (x[1]*y[1])

    #print(dict_)

    ans = list(map(lambda x: dict_[x],dict_))[::-1]
    #print(ans)
    return ans

    #print(p1wp,p2wp)

if __name__ == "__main__":
    multiply_polynomials([1],[])
    multiply_polynomials([1,1.5],[1])
    multiply_polynomials([2],[2])
    multiply_polynomials([2,0,3],[4,5])
    assert multiply_polynomials([2,0,3],[4,5]) == [8, 10, 12, 15]
    assert multiply_polynomials([4,5],[2,0,3]) == [8, 10, 12, 15]
    multiply_polynomials([2,5,1],[1,2,1])
