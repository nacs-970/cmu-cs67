#!/usr/bin/env python3
# Atithep Thepkij 
# 670510681
# HW13_3
# 204111 Sec 002
def sum_d_product(m:list[list[int]]) -> int:
    if len(m) == 1:
        return m[0][0]
    res = []
    for i in range(len(m)):
        if i%2 == 0:
            list_ = m[i]
        if i%2 == 1:
            even = list(map(lambda x,y: x*y, list_[::2], m[i][1::2]))
            odd = list(map(lambda x,y: x*y, list_[1::2], m[i][::2]))
            res += [list(map(lambda x,y: x+y, even, odd))]
    return sum_d_product(res)

def sum_d_product2(m2: list[list[int]]) -> int:
    from copy import deepcopy
    m = deepcopy(m2)
    if len(m) == 2:
        return m[0][0] * m[1][1] + m[1][0] * m[0][1]

    results = []
    for i in range(0, len(m), 2):
        result = []
        while m[i]:
            dot_product = m[i][0] * m[i + 1][1] + m[i][1] * m[i + 1][0]
            result.append(dot_product)
            m[i] = m[i][2:]
            m[i + 1] = m[i + 1][2:]
        results.append(result)
        
    return sum_d_product2(results)

def test():
    import random,copy
    for _ in range(100):
        sqrt = 2**(random.choice(range(1,10)))
        set_ = set(range(sqrt))
        l = [ [ random.randint(0,999) for _ in set_ ] for _ in set_ ]
        #for i in set(range(sqrt)):
        #    tmp = []
        #    for j in set(range(sqrt)):
        #        tmp += [random.randint(0,999)]
        #    l += [tmp]
        try:
            assert sum_d_product2(l) == sum_d_product(l)
        except:
            print(l2)
            print(sum_d_product2(l))
            print(sum_d_product(l))
            return 0
if __name__ == "__main__":
    test()
    print(":o;")