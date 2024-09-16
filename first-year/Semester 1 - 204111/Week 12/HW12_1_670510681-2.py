#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_1
# 204111 Sec 002

import time

def scramble(word):
    #p = [[]] * len(word)
    #word = list(word)
    #ans = set()

    #while word:
    #    str_ = word[0]
    
    def permutation(word,str_="",ans=set()):
        if len(word) == 0 or not word:
            ans.add(str_)
            return ans

        if len(str_) == len_w - 1 and str_ in ans:
            str_ = ""

        #print(word)
        #if str_ + word[0] in ans or word[0] + str_ in ans:
        #    str_ = ""


        else:
            for i in range(len(word)):
                permutation(word[:i] + word[i+1:],str_ + word[i])
                #permutation(word[:i] + word[i+1:],word[i] + str_)
                #permutation(word[:i][::-1] + word[i+1:][::-1],str_ + word[i])
                #permutation(word[:i][::-1] + word[i+1:][::-1],word[i] + str_)

                # 1 / 0
                # 0 permuation( "" + "23" , "" + 1)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "13" + 2)
                # 2 / 1
                # 0 permuation( "1" + "2" , from 1/0 + 2)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "1a3" + 2)
                # .. n

        return ans

    len_w = len(word)

    #for i in word:
    #    c = word.count(i)
    #    if c == len_w:
    #        return [word]

    start = time.time()
    return list(permutation(word))
    #return print(list(permutation(word))),print(f"{time.time() - start:.07f}")


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
    #scramble("1")
    #scramble("12")
    #scramble("123")
    #scramble("Cat")
    #scramble("bee")
    #scramble("bEe")
    #scramble("1234")
    #scramble("333333333")
    #scramble("3333333333")
    #scramble("123456789")
    scramble("111111110")
    scramble("1234567890")
    #start = time.time()
    #print(f'{time.time() - start:.07f}')
