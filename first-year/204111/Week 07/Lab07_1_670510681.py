#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Lab07_1
# 204111 Sec 002

def corner_frame(n:int) -> str: # str (n>=2)

    number = list(range(1,n+1))

    len_ = len(number)
    corner = list(map(lambda x: (x*[x])+number[-len_+x:],number)) # repeat(num * num) + ordering number without start of the index 
    #corner = list(map(lambda x: str((x*[x])+number[-len_+x:]),number))
    del corner[-1][len_:] # n = 7 coner[-1] = [77777771234567]

    corner = list(map(lambda x: str(x),corner))
    corner = list(map(lambda x: x.strip('[]'),corner))
    #corner = list(map(lambda x: x,range_))
    corner = '\n'.join(corner).replace(',','')+'\n'
    return corner

def test():
    assert corner_frame(4) == """1 2 3 4
2 2 3 4
3 3 3 4
4 4 4 4
"""
    assert corner_frame(7) == """1 2 3 4 5 6 7
2 2 3 4 5 6 7
3 3 3 4 5 6 7
4 4 4 4 5 6 7
5 5 5 5 5 6 7
6 6 6 6 6 6 7
7 7 7 7 7 7 7
"""
    print("\[ - v - \ ]")

if __name__ == "__main__":
    test()
