#!/usr/bin/env python3
# ชื่อ (ไม่ต้องใส่นามสกุล)
# รหัสนศ
# Sec00x

def log2_list(list_a):
    list_ = list(map())


from math import isclose
if __name__ == '__main__':

    list_a = [1, 2, 4]
    log2_list(list_a)
    assert all(map(lambda x, y: isclose(x, y, abs_tol=0.001),
                   list_a, [0.0, 1.0, 2.0]))

    print("All OK!")
