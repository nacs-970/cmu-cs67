#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_1
# 204111 Sec 002

import time

def scramble(word):
    len_w = len(word)
    str_ = ""
    str_2 = ""
    ans = set()
    for i in range(len(word)):
        str_ = word[i];str_2 = word[i]

        for j in word[:i] + word[i+1:]:
            str_ = str_ + j

        ans.add(str_)

        for j in word[i+1:] + word[:i]:
            str_2 = str_2 + j

        ans.add(str_2)

    print(ans)
    #print(any(list(d.keys())))
    #print(not any([0,0]))

if __name__ == "__main__":
    scramble("1")
    scramble("12")
    scramble("123")
    scramble("Cat")
    scramble("bee")
    scramble("bEe")
    scramble("1234")
    #start = time.time()
    #scramble("1234567890")
    #print(f'{time.time() - start:.07f}')
