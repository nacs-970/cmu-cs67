#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_1
# 204111 Sec 002
import time

def scramble(word):

    def permutation(word):

        #now = float(f"{time.time() - start:.07f}")
        #print(now)
        #if now >= 6:
        #    print("too slow")
        #    return

        #if len(word) == 1:

        if len(word) == 1:
            #ans.add(tuple(str_))
            return [word]

        #print(word)

        next_ = permutation(word[1:]) # split to base case
        #print(next_)
        now = word[0]
        ans = set()

        for char in next_: # from base case
            for j in range(len(char) + 1): # _1_2_3_ len = 3, So len + 1

                # add now between
                str_ = char[:j] + now + char[j:]
                ans.add(str_)
                #if len(str_) == len_w:
                #print(i[:j] + now + i[j+1:])
        #print(str_)
        return ans

        #permutation(word[:i] + word[i+1:], word[i] + str_ )

    start = time.time() 
    #len_w = len(word)
    #ans = permutation(word)
    #ans = list(filter(lambda x: len(x) == len_w,permutation(word)))
    #print(ans)
    #return list(ans)
    ans = permutation(word)
    ans = list(ans)
    end = time.time() 

    #print(sorted(permutation(word)))
    #print(f"{end - start:.07f}")
    return ans#,print(f"{end - start:.07f}")
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
