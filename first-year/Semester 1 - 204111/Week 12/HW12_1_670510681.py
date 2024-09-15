#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_1
# 204111 Sec 002

def scramble(word):

    def permuation(remain,word="",):

        if len(remain) == 0:
            ans.add(word)

        else:
            for i in range(len(remain)):
                permuation(remain[:i] + remain[i+1:],word + remain[i])
                # 1 / 0
                # 0 permuation( "" + "23" , "" + 1)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "13" + 2)
                # 2 / 1
                # 0 permuation( "1" + "2" , from 1/0 + 2)
                # 1 permuation( "1" + "3" , "1" + 2)
                # 2 permuation( "12" + "3" , "13" + 2)
                # .. n

    ans = set()
    permuation(word)
    
    #print(sorted(ans))
    return sorted(ans)


if __name__ == "__main__":
    scramble("Cat")
    scramble("bee")
    scramble("bEe")
