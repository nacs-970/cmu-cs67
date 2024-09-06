#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# Lab10_1
# 204111 Sec 002

def comma_separated(n:int,group: int=3):
    n = str(n)
    range_ = list(range(-len(n),0,group)) # start from behind
    #print(range_)
    str_ = list(n)
    str_ = list(map(lambda x: f',{str_[x]}' if -x in range_ else str_[x],range(len(n))))
    #print(str_)
    return ''.join(str_)

if __name__ == "__main__":
    n = 1234
    g = 1
    #n = 1000 # 1,000
    #g = 3
    print(comma_separated(n,g))

