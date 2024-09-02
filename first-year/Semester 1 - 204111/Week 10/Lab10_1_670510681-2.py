#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# Lab10_1
# 204111 Sec 002

# not finish yet!
def comma_separated(n:int,group: int=3):
    n = str(n)
    range_ = list(range(-(len(n)),0,group))
    return range_
    str_ = ""
    while len(n) != 0:
        if len(n)%group == 0 and str_ != "":
            str_ += ","
        str_ += n[0]
        n = n[1:]
    return str_
if __name__ == "__main__":
    n = 1000000 # 100,0000
    g = 4
    #n = 1000 # 1,000
    #g = 3
    print(comma_separated(n,g))

