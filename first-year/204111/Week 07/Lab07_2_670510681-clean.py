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
    
    body =  range_[n:] # 05 -> 12
    index_ = list(range(n-2)) # 05(0) 06(1) 00 00 00 00 11(-2) 12(-1)
    body = list(map(lambda x: [body[-(x+1)]]+(n-2)*[max_*sep]+[body[x]],index_)) # 12(-1) 11(-2) max_*[sep_] 05(0) 06(1)

    bottom = range_[n:] # 05 -> 12
    bottom = bottom[n-2:-(n-2)][::-1]# reverse , cannot [n-2:-(n-2):-1] because will be ' '
    # body = [[12,'  ','  ',05],[11,'  ','  ',06]]
    body_print = list(map(lambda x:sep.join(body[x]),range(len(body))))
    ans = sep.join(top)+'\n'+'\n'.join(body_print)+'\n'+sep.join(bottom)

    print(ans)
    return ans


def test():
    return 0

if __name__ == "__main__":
    square_frame(4)
    square_frame(30,'.')
    square_frame(30)
    square_frame(10)
    square_frame(20,'.')
