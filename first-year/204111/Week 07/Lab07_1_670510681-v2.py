#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Lab07_1
# 204111 Sec 002

DEBUG = True

def corner_frame(n:int) -> str:
    # one line no zfill
    #return '\n'.join(list(map(lambda x: str(x).strip('[]'),list(map(lambda x: (x-1)*[x]+list(range(1,n+1))[x-1:],list(range(1,n+1))))))).replace(',','')+'\n'
    
    number = list(range(1,n+1))
    corner = list(map(lambda x: (x-1)*[x]+number[x-1:],number))
    corner = list(map(lambda x: str(x).strip('[]'),corner))
    corner = '\n'.join(corner).replace(',','')+'\n'
    
    if DEBUG == True: print(corner)
    return corner
    
def corner_frame_zfill(n:int) -> str: # str (n>=2)

    
    # zfill
    max_ = len(str(n))
    
    number = list(range(1,n+1))
    number = list(map(lambda x: str(x).zfill(max_),number))
    index_ = list(range(n))
    
    #return print(corner)
    corner = list(map(lambda x: x*[number[x]]+number[x:], index_))
    corner = list(map(lambda x: " ".join(corner[x]), index_))
    #corner = list(map(lambda x: corner[x].strip('[]'),index_))
    corner = "\n".join(corner)
    if DEBUG == True: print(corner)
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
    corner_frame(10)
    print("--------")
    corner_frame_zfill(100)
