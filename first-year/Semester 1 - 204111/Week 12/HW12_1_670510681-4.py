#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_1
# 204111 Sec 002
import time

def scramble(word: str) -> list[str]:
    ans = {''}
    for char in word: # loop with each character in word
        str_ = set()
        for pattern in ans: # get all possibility to add char from ans
            for index_ in range(len(pattern) + 1): # slice pattern to insert char in the between
                str_.add(pattern[:index_] + char + pattern[index_:])
        ans = str_
    return list(ans)

if __name__ == "__main__":
    #scramble("1")
    scramble("12")
    scramble("123")
    scramble("Cat")
    scramble("bee")
    scramble("bEe")
    scramble("1234")
    scramble("1234567890")
    scramble("1234567890")
