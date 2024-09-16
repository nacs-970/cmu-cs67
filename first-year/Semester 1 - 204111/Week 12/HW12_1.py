#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_1
# 204111 Sec 002
import time
def scramble(word):

    def permuation(remain,word="",ans=set()):

        if not remain:
            ans.add(word)

        else:
            for i in range(len(remain)):
                permuation(remain[:i] + remain[i+1:],word + remain[i])

        return ans
                # 1 / 0
                # 0 permuation( "" + "23" , "" + 1)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "13" + 2)
                # 2 / 1
                # 0 permuation( "1" + "2" , from 1/0 + 2)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "13" + 2)
                # .. n

    start = time.time() 
    if len(word) <= 1:
        return [word]

    #ans = permuation(word)
    #end = time.time() 

    #print(sorte(ans))
    #print(f"{end - start:.07f}")
    return list(permuation(word))
    #return list(ans),print(f"{time.time() - start:.07f}")


if __name__ == "__main__":
    scramble("1")
    scramble("12")
    scramble("123")
    scramble("Cat")
    scramble("bee")
    scramble("bEe")
    scramble("1234567890")
