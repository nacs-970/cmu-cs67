#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# Lab10_2
# 204111 Sec 002

def longest_digit_run(n: int) -> int:
    #range_ = range(len(str(n)))
    n = str(n)
    count = []
    temp = 0
    #list_ = list(map( lambda x: n[x] if n[x] != n[x+1] else n[x+1],range_))
    #return list_
    while len(n) != 0:
        #print(n)
        if len(n) == 1 or n[0] != n[1]:
            temp += 1
            count.append(temp)
            temp = 0
            n = n[1:]
        else:
            temp += 1
            n = n[1:]
    return max(count)


if __name__ == "__main__":
    n = 113377722
    print(longest_digit_run(n))

