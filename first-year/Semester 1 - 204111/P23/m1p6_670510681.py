#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Sec 002
def harmonic_mean(list_a):
    def divided(list_): 
        if len(list_) == 0:return 0
        now = 1/list_[0]
        next_ = divided(list_[1:])
        return now + next_
    #print(len(list_a) / divided(list_a))
    return len(list_a) / divided(list_a)

from math import isclose
if __name__ == '__main__':
    assert isclose(harmonic_mean([1, 2, 2, 2]), 1.6, abs_tol=0.001)

    print("All OK!")
