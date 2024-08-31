#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW08_2
# 204111 Sec 002

import string

def is_anagram(s1_b:str,s2_b:str) -> True:
    s1,s2 = s1_b.lower(),s2_b.lower()
    s1 = list(filter(lambda x: x.isalpha(),s1)) 
    s2 = list(filter(lambda x: x.isalpha(),s2)) 

    if len(s1) != len(s2): return False
    
    # not necessary
    #max_,min_ = max(s1,s2),min(s1,s2)
    #range_ = range(len(min_)) 
    #compare_min = list(map(lambda x: min_[x] in max_,range_))
    #compare_max = list(map(lambda x: max_[x] in min_,range_))
    #if False in compare_min or False in compare_max: return False

    # a - z : 26
    aiiz = string.ascii_lowercase
    count_s1 = list(map(lambda x: s1.count(aiiz[x]),range(26)))
    count_s2 = list(map(lambda x: s2.count(aiiz[x]),range(26)))
    if count_s1 != count_s2: return False
    return True

    #s1 = reduce(lambda x,y: x != y,s1)
    #return s1

if __name__ == "__main__":
    print(is_anagram('Eleven plus two','Twelve plus one'))
    print(is_anagram('Eleven plxs two','Twelve plus one'))
    print(is_anagram('cat','tab'))
    print(is_anagram('aa','aa'))
    print(is_anagram('ac','aa'))
    print(is_anagram('a','aa'))
    print(is_anagram('Nissan','Insane'))
