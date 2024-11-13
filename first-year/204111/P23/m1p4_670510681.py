#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Sec 002
import math 
def log2_list(list_a):
    list_a[:] = list(map(lambda x: math.log2(x),list_a))

    
from math import isclose
if __name__ == '__main__':

    list_a = [1, 2, 4]
    log2_list(list_a)
    assert all(map(lambda x, y: isclose(x, y, abs_tol=0.001),
                   list_a, [0.0, 1.0, 2.0]))

    print("All OK!")
