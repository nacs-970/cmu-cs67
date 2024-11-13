#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# Lab10_1
# 204111 Sec 002

def comma_separated(n:int,group: int=3):
    n = str(n)
    str_ = ""
    while len(n) != 0:
        if len(n)%group == 0 and str_ != "":
            str_ += ","
        str_ += n[0]
        n = n[1:]
    return str_
    
def comma_separated2(n:int,group: int=3):
    n = str(n)
    range_ = list(range(-len(n),0,group)) # start from behind
    #print(range_)
    str_ = list(n)
    str_ = list(map(lambda x: f',{str_[x]}' if -x in range_ else str_[x],range(len(n))))
    #list(map(lambda x: str_.insert(-x,','),range_))
    #print(str_)
    return ''.join(str_)
    
import random
def test():
    for i in range(1000000):
        n,c = random.randint(0,100000000),random.randint(1,10)
        try:
            assert comma_separated2(n,c) == comma_separated(n,c)
        except:
            print(n,c)
            print(comma_separated2(n,c))
            print(comma_separated(n,c))
            return 0
    print("f u f")
if __name__ == "__main__":
    n = 1000000
    g = 4
    #print(comma_separated(n))
    test()

