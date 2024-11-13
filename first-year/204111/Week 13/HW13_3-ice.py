#!/usr/bin/env python3
# Atithep Thepkij 
# 670510681
# HW13_3
# 204111 Sec 002

def sum_d_product(m2: list[list[int]]) -> int:
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
        
    return sum_d_product(results)
if __name__ == "__main__":
    assert sum_d_product([[3,3,3,2],[2,0,3,1],[2,1,2,3],[1,0,2,-1]]) == 33
    assert sum_d_product([[0, -1, -1, 3, 2, 3, -1, 3],[3, -1, -1, 2, 0, -1, 2, 1],[3, 0, 1, 2, 3, 1, 3, 1],[2, 2, 1, -1, -1, 2, 0, 3],[1, 3, 2, 1, 3, 2, 2, 1],[1, 2, 2, 1, 3, 3, 1, 3],[2, 2, 2, 2, 2, 2, 3, 3],[1, 3, 2, 3, 1, 1, 2, 2]]) == -6290
    m = [[1, 1, 5, -1],[12, 2, -2, 0],[4, 8, 8, 12],[4, 12, 12, 15]]
    print(sum_d_product(m))