#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# Lab12_2
# 204111 Sec 002

def multiply_polynomials(p1: list[int], p2: list[int]) -> list[int]:
    if not p1 and not p2: return []
    if not p1 or not p2: return max(p1,p2)

    # start from behind [2,0,3] -> 2x^2 + 0x^1 + 3x^0
    p1wp = list(filter(lambda x: type(x) == int,p1)) 
    p2wp = list(filter(lambda x: type(x) == int,p2)) 

    # insert power | power, coeff
    p1wp = list(map(lambda x,y: [x,y],range(len(p1wp)-1,-1,-1),p1wp))
    #p1wp = list(filter(lambda x: x[1] != 0,p1wp))

    p2wp = list(map(lambda x,y: [x,y],range(len(p2wp)-1,-1,-1),p2wp))
    #p2wp = list(filter(lambda x: x[1] != 0,p2wp))

    #print(p1wp,p2wp)
    #p1 = list(filter(lambda x: x != 0,p1))
    #p2 = list(filter(lambda x: x != 0,p2))

    max_,min_ = max(p1wp,p2wp),min(p1wp,p2wp)
    res = []

    for x in max_:
        #print(x)
        for y in min_:
            #print(x,"*",y)
            res.append([x[0]+y[0],x[1]*y[1]])

    #print(res)

    #ans = sorted(ans,key = lambda x: x[1], reverse = True) 
    #print(ans)

    res = sorted(res,key = lambda x: x[0], reverse = True) 
    dict_ = dict(map(lambda x: (x[0],0),res))

    for n in res:
        dict_[n[0]] += n[1]

    #print(dict_)
    ans = list(map(lambda x: dict_[x],dict_))

    #ans = list(map(lambda x: x[1],ans))
    #ans = list(filter(lambda x: x != 0,ans))
    return ans

    #print(p1wp,p2wp)

if __name__ == "__main__":
    #multiply_polynomials([1],[])
    #multiply_polynomials([1,1.5],[1])
    #multiply_polynomials([2],[2])
    multiply_polynomials([2,0,3],[4,5])
    assert multiply_polynomials([2,0,3],[4,5]) == [8, 10, 12, 15]
    assert multiply_polynomials([4,5],[2,0,3]) == [8, 10, 12, 15]
    multiply_polynomials([2,5,1],[1,2,1])
