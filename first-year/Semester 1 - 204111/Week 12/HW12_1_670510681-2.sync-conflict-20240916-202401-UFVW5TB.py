#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_1
# 204111 Sec 002

import time
start = time.time()
import math

def scramble(word):
    #p = [[]] * len(word)
    #word = list(word)
    #ans = set()

    #while word:
    #    str_ = word[0]
    
    def permutation(word,str_="",ans=set()):

        if not word:
            ans.add(str_)

        else:
            for i in range(len(word)):
                permutation(word[i:] + word[:i+1],str_ + word[i])
                permutation(word[i:] + word[:i+1],word[i] + str_)

        return ans

    print(permutation(word))


        #for j in word[:i] + word[i+1:]:
        #    str_ = str_ + j
        #ans.add(str_)

        #str_ = word[i]
        #for j in word[:i] + word[i+1:]:
        #    str_ = str_ + j
        #ans.add(str_)

        #str_ = word[i]
        #for j in word[:i] + word[i+1:]:
        #    str_ = j + str_
        #ans.add(str_)

        #str_ = word[i]
        #for j in word[i+1:] + word[:i]:
        #    str_ = str_ + j
        #ans.add(str_) 

        #str_ = word[i]
        #for j in word[i+1:] + word[:i]:
        #    str_ = j + str_
        #ans.add(str_)

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
