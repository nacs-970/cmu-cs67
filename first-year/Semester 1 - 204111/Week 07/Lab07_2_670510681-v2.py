#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# Lab07_2
# 204111 Sec 002

def square_frame(n:int,sep: str=' ') -> str: # str (n>=3) and don't use sep_ 

    space = (n-2)**2 # find a space in square
    range_ = list(range(1,((n**2)-space)+1))
    max_ = len(str(range_[-1]))
    range_ = list(map(lambda x: str(x).zfill(max_),range_))
    
    top = range_[:n]
    top = sep.join(top)
    right = range_[n:(2*n)-2]
    left = range_[-1:-(n-1):-1]
    #lr = [*zip(left,right)] # vertical list 
    left_right = list(zip(left,right))
    mid = list(map(lambda x: (((n-1)+((n-2)*max_))*sep).join(x),left_right))
    mid = '\n'.join(mid)
    bottom = range_[(2*n)-2:(3*n)-2]
    bottom = sep.join(bottom)
    ans = top+'\n'+mid+'\n'+bottom
    print(ans)


def test():
    return 0

if __name__ == "__main__":
    square_frame(4,'.')
    square_frame(3)
    square_frame(10)
    square_frame(20,'.')