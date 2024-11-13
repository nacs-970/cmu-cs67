#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_1
# 204111 Sec 002
import time

def scramble(word):

    def permutation(word):

        if len(word) == 1:
            return [word]

        next_ = permutation(word[1:]) # split to base case
        now = word[0]
        ans = set()

        for char in next_: # from base case
            for j in range(len(char) + 1): # _1_2_3_ len = 3, So len + 1

                str_ = char[:j] + now + char[j:]
                ans.add(str_)

        return ans

    start = time.time() 
    ans = permutation(word)
    ans = list(ans)
    end = time.time() 
    #print(ans)
    return ans,print(f"{end - start:.07f}")
    #return print(sorted(permutation(word))),print(f"{end - start:.07f}")

if __name__ == "__main__":
    #scramble("1")
    scramble("12")
    scramble("123")
    scramble("Cat")
    scramble("bee")
    scramble("bEe")
    scramble("1234")
    scramble("1234567890")
