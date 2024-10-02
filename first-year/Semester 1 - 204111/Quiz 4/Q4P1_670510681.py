#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Sec002

DEBUG = False

def projections(n: int, opaque_cells: list[tuple[int]]) -> dict[str, list[list[int]]]:
    # x,y,z top down
    result = {}

    xy = [[0]*n for _ in range(n)]
    xz = [[0]*n for _ in range(n)]
    yz = [[0]*n for _ in range(n)]

    for block in opaque_cells:
        x,y,z = block
        xy[y][x] = 1
        xz[z][x] = 1
        yz[z][y] = 1

    result["xy"] = xy
    result["xz"] = xz
    result["yz"] = yz

    if DEBUG: pretty_print_dict(result)

    return result


def pretty_print_dict(data: dict):

    print("{")
    for key, value in data.items():
        print(f'  "{key}": [')
        for row in value:
            print(f'    {row},')
        print("  ]")
    print("}")


if __name__ == '__main__':
    projections(4, [(0, 0, 0), (2, 1, 3)])
    projections(5, [(3, 1, 3), (3, 1, 4),(3, 2, 4), (3, 3, 4)])
    assert projections(4, [(0, 0, 0), (2, 1, 3)]) ==  {
    'xy': [[1, 0, 0, 0],
           [0, 0, 1, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0]],
    'xz': [[1, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 1, 0]],
    'yz': [[1, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 0, 0, 0],
           [0, 1, 0, 0]]
    }

    print('ALL OK')
