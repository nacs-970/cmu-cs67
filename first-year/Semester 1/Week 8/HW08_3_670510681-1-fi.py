#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW08_2
# 204111 Sec 002

def is_anagram(s1_b:str,s2_b:str) -> True:
    s1,s2 = s1_b.lower(),s2_b.lower()

    # filter alpha
    s1 = list(filter(lambda x: x.isalpha(),s1)) 
    s2 = list(filter(lambda x: x.isalpha(),s2)) 

    if len(s1) != len(s2):return False
    if s1 == [] or s2 == []:return False

    len_s1 = len(s1)-1
    len_s2 = len(s2)-1
    
    # Sort str in list
    def sort_str(list_,index_):
        if index_ == 0:return list_
        now = list_[index_]
        next = sort_str(list_,index_-1)
        if now < list_[index_-1]:
            list_[index_-1],list_[index_] = list_[index_],list_[index_-1]

        return sort_str(list_,index_-1)
    #s1_sort = sort_str(s1,len_s1)
    #2_sort = sort_str(s2,len_s2)
    def sort_str(list_,n=0):
        if len(list_)-1 == n:return list_
        now = list_[n]
        next_ = list_[n+1]
        if now < next_:now,next_ = next_,now
        return(list_,n+1)

    s1_sort = sort_str(s1)
    s2_sort = sort_str(s2)
    print(s1_sort,s2_sort)
    return s1_sort == s2_sort

if __name__ == "__main__":
    print(is_anagram('Eleven plus two','Twelve plus one'))
    print(is_anagram('Eleven plxs two','Twelve plus one'))
    print(is_anagram('cat','tab'))
    print(is_anagram('aa','aa'))
    print(is_anagram('ac','aa'))
    print(is_anagram('a','aa'))
    print(is_anagram('',''))
    print(is_anagram('Nissan','Insane'))
