#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Sec002

def wet_area(m: int, n: int, v: int,sprinkler_list: list[tuple[int, int]]) -> dict[tuple[int, int], int]:
    dict_ = {}
    #board = [[0]*m for _ in range(n)]
    rows,cols = m,n
    sprinkler_set = set(sprinkler_list) 

    for sprinkler in sprinkler_set:
        x,y = sprinkler

        vaild_check = lambda x,y: x <= rows - 1 and x >= 0 and y <= cols - 1 and y >= 0
        around = set([(x-v,y), (x+v,y), (x,y+v), (x,y-v)])

        for value in set(range(1,v+1)):
            around.add((x - value,y))
            around.add((x + value,y))
            around.add((x,y + value))
            around.add((x,y - value))


        for s in around:
            if not vaild_check(s[0],s[1]) or s in sprinkler_set:
                continue
            if vaild_check(s[0], s[1]):
                dict_[s] = dict_.get(s,0) + 1

    #print(dict_)
    return dict_


if __name__ == '__main__':
    assert wet_area(4, 5, 1, [(0, 0), (1, 2),(1, 3), (3, 2)]) == {(0, 1): 1, (0, 2): 1, (0, 3): 1,(1, 0):1, (1, 1):1, (1, 4):1, (2,2): 2, (2, 3):1, (3, 1): 1, (3,3):1}
