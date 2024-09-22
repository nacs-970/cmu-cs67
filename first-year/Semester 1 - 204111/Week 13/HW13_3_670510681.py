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
            #res += [even,odd]
            res += [list(map(lambda x,y: x+y, even, odd))]
    #print(res)
    return sum_d_product(res)
if __name__ == "__main__":
    assert sum_d_product([[3,3,3,2],[2,0,3,1],[2,1,2,3],[1,0,2,-1]]) == 33
    assert sum_d_product([[0, -1, -1, 3, 2, 3, -1, 3],[3, -1, -1, 2, 0, -1, 2, 1],[3, 0, 1, 2, 3, 1, 3, 1],[2, 2, 1, -1, -1, 2, 0, 3],[1, 3, 2, 1, 3, 2, 2, 1],[1, 2, 2, 1, 3, 3, 1, 3],[2, 2, 2, 2, 2, 2, 3, 3],[1, 3, 2, 3, 1, 1, 2, 2]]) == -6290
    m = [[1, 1, 5, -1],[12, 2, -2, 0],[4, 8, 8, 12],[4, 12, 12, 15]]
    print(sum_d_product(m))