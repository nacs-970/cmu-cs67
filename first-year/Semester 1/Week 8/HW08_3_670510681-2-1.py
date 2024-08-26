#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW08_2
# 204111 Sec 002

def is_anagram(s1_b:str,s2_b:str) -> True:
    s1,s2 = s1_b.lower(),s2_b.lower()
    s1 = list(filter(lambda x: x.isalpha(),s1)) 
    s2 = list(filter(lambda x: x.isalpha(),s2)) 

    if len(s1) != len(s2): return False
    
    # same lenght
    #max_,min_ = max(s1,s2),min(s1,s2)
    #range_ = range(len(min_)) 
    # slower than recursive
    #compare_min = list(map(lambda x: min_[x] in max_,range_))
    #compare_max = list(map(lambda x: max_[x] in min_,range_))
    #if False in compare_min or False in compare_max: return False
    
    # same lenght
    def count_str(list_a,list_b,index_):
        #print(list_a,list_b,index_)
        # if index_ == 0 and list_a[index_]
        if list_b == []:return True
        if list_a[index_] not in list_b: return False
        list_b.remove(list_a[index_])
        return count_str(list_a,list_b,index_-1)
        
    len_ = len(s1)-1 # index
    return count_str(s1,s2,len_)

if __name__ == "__main__":
    print(is_anagram('Eleven plus two','Twelve plus one'))
    print(is_anagram('Eleven plxs two','Twelve plus one'))
    print(is_anagram('cat','tab'))
    print(is_anagram('aa','aa'))
    print(is_anagram('ac','aa'))
    print(is_anagram('sba','bas'))
    print(is_anagram('sxba','baos'))
    print(is_anagram('eeee','eeee'))
    print(is_anagram('a','aa'))
    print(is_anagram('Nissan','Insane'))
