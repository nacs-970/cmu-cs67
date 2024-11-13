#!/usr/bin/env python3
# Atithep Thepkij 
# 670510681
# HW12_3
# 204111 Sec 002

def main():
    bomb = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
    print(print_board(500,500,bomb))
    #assert ms_mine_hint(4, 4, bomb) == {(0, 0): 1, (0, 2): 2, (1, 0): 3, (1, 1): 5}
    print("OK")

# row -> | col v
def ms_mine_hint(m: int, n: int, bomb_list: list[tuple[int]]) -> dict[tuple[int], int]:
    row = list(range(m))
    col = list(range(n))
    
    d = dict()
    #print(row,col)

    for x in row:
        for y in col:
            sum = 0

            if (x,y) in bomb_list: continue
            if (x,y+1) not in bomb_list and (x,y-1) not in bomb_list and (x-1,y) not in bomb_list and (x+1,y) not in bomb_list and (x-1,y-1) not in bomb_list and (x+1,y-1) not in bomb_list and (x-1,y+1) not in bomb_list and (x+1,y+1) not in bomb_list:
                continue

            # top
            if (x,y+1) in bomb_list:
                sum += 1
            # bottom
            if (x,y-1) in bomb_list:
                sum += 1

            # left
            if (x-1,y) in bomb_list:
                sum += 1
            # right
            if (x+1,y) in bomb_list:
                sum += 1

            # up left
            if (x-1,y-1) in bomb_list:
                sum += 1
            # up right
            if (x+1,y-1) in bomb_list:
                sum += 1

            # down left
            if (x-1,y+1) in bomb_list:
                sum += 1
            # down right
            if (x+1,y+1) in bomb_list:
                sum += 1

            d[(x,y)] = sum

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
