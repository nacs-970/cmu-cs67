#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# Lab10_2
# 204111 Sec 002

# not finish yet!

def longest_digit_run(n: int) -> int:
    if n <= 9:return 1
    range_ = range(len(str(n)))
    n = str(n) + "*"
    list_ = list(map(lambda x: n[x] if n[x] == n[x+1] else "",range_))
    list_ = list(filter(lambda x: x != "",list_))
    list_ = list(map(lambda x: list_.count(x),list_))
    if list_ == []:
        return 1
    return max(list_)

def longest_digit_run2(n: int) -> int:
    n = str(n)
    count = []
    temp = 0
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

import random
def test():
    for i in range(1000):
        n = random.randint(0,999999999999999999)
        try:
            assert longest_digit_run(n) == longest_digit_run2(n)
        except:
            print(n)
            print(longest_digit_run2(n))
            print(longest_digit_run(n))
            return 0
if __name__ == "__main__":
    #test()
    n = 111777888
    #n = 693822812206238296
    print(longest_digit_run(n))

