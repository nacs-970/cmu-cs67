#!/usr/bin/env python3
# ชื่อ (ไม่ต้องใส่นามสกุล)
# รหัสนศ
# Sec00x

DEBUG = False


def projections(n: int, opaque_cells: list[tuple[int]]) -> dict[str, list[list[int]]]:

    result = {}

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
