#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_1
# 204111 Sec 002

import time
def scramble(word):

    def permutation(word,str_="",ans=set()):

        #now = float(f"{time.time() - start:.07f}")
        #print(now)
        #if now >= 6:
        #    print("too slow")
        #    return

        if len(str_) == len_w - 1 and str_ in ans:
            str_ = ""

        if not word:
            ans.add(str_)

        else:
            for i in range(len(word)):
                permutation(word[:i] + word[i+1:], str_ + word[i])
                permutation(word[:i] + word[i+1:], word[i] + str_ )

        return list(ans)

                # 1 / 0
                # 0 permuation( "" + "23" , "" + 1)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "13" + 2)
                # 2 / 1
                # 0 permuation( "1" + "2" , from 1/0 + 2)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "1a3" + 2)
                # .. n

    start = time.time() 

    len_w = len(word)

    if len(word) <= 1:
        return [word]

    #ans = permuation(word)
    #end = time.time() 

    print(sorted(permutation(word)))
    #print(f"{end - start:.07f}")
    #return list(permuation(word))#,print(f"{time.time() - start:.07f}")


if __name__ == "__main__":
    scramble("1")
    scramble("12")
    scramble("123")
    scramble("Cat")
    scramble("bee")
    scramble("bEe")
    scramble("1234")
    #scramble("123456789AB")