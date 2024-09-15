#!/usr/bin/env python3
# Atithep Thepkij 
# 670510681
# HW12_3
# 204111 Sec 002

import random
import time

def main():
    bomb = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    assert ms_mine_hint(3, 3, bomb) == {(0, 0): 1, (0, 2): 2, (1, 0): 3, (1, 1): 5}

    bomb = []
    row,col = random.randint(3,500),random.randint(3,500)
    #print(print_board(4,4,bomb))
    for i in range(random.randint(1,row*col)):
        b = [(random.randint(0,row-1), random.randint(0,col-1))]
        if b in bomb:
            continue
        bomb += b
    print(row,col,bomb,len(bomb))

    start = time.time()
    ms_mine_hint(row,col,bomb)
    print(f"{time.time() - start:.010f}")

    print("OK")

# row -> | col v
def ms_mine_hint(m: int, n: int, bomb_list: list[tuple[int]]) -> dict[tuple[int], int]:
    #row = list(range(m))
    #col = list(range(n))

    base = set(bomb_list)
    row,col = m,n 
    d = dict()
    #skip = set()
    #print(row,col)

    #while bomb_list:
        #x = bomb_list[0][0]
        #y = bomb_list[0][1]
        #print(bomb_list[0])

        #if (x,y) in skip:
        #    bomb_list = bomb_list[1:]
        #    continue
    for i in base:
        x = i[0]
        y = i[1]


        vaild_check = lambda x,y: x <= row - 1 and x >= 0 and y <= col - 1 and y >= 0
        around = set([(x-1,y),(x+1,y),(x,y+1),(x,y-1),(x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)])

        for i in around:
            #print(i,i in base)
            if i in base or not vaild_check(i[0],i[1]):
                #skip.add(i)
                continue

            if vaild_check(i[0],i[1]):
                d[i] = d.get(i,0) + 1

        #bomb_list = bomb_list[1:]

    #print(d)
    return d


def print_board(n_row, n_col, b_list):
    max_len = len(str(max(n_row, n_col)))
    pad = ' '
    board_str = []
    board_str += [pad + pad*(max_len) +
                  pad.join(map(lambda x: str(x).zfill(max_len), range(n_col)))]

    for i in range(n_row):
        for j in range(n_col):
            if j == 0:
                temp = str(i).zfill(max_len) + pad
            pad2 = ' ' * (max_len - 1)
            if (i, j) in b_list:
                temp += pad2 + 'B' + pad
            else:
                temp += pad2 + '.' + pad
        board_str += [temp.rstrip()]

    print('\n'.join(board_str))


if __name__ == "__main__":
    main()
