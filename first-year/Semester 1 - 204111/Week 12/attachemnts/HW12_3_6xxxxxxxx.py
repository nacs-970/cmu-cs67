#!/usr/bin/env python3
# ชื่อ นามสกุล (ชื่อเล่น)
# 6XXXXXXXX
# HW12_3
# 204111 Sec 00?

def main():
    assert ms_mine_hint(3, 3, [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]) == \
        {(0, 0): 1, (0, 2): 2, (1, 0): 3, (1, 1): 5}
    print("OK")


def ms_mine_hint(m: int, n: int, bomb_list: list[tuple[int]]) -> dict[tuple[int], int]:
    d = dict()

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
