#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW08_2
# 204111 Sec 002

def is_anagram(s1_b:str,s2_b:str) -> True:

    # Filter
    s1,s2 = s1_b.lower(),s2_b.lower()
    s1 = list(filter(lambda x: x.isalpha(),s1)) 
    s2 = list(filter(lambda x: x.isalpha(),s2)) 

    if len(s1) != len(s2): return False
    
    # Same lenght
    def check_ (list_a,list_b):
        #print(list_a,list_b)
        # if True list will be empty list
        if list_a == []: return True
        str_ = list_a[0]
        # have same
        if str_ in list_b:
            # remove same
            list_b.remove(str_)
            return check_(list_a[1:],list_b) # next char in list_a
        return False

    return check_(s1,s2)

if __name__ == "__main__":
    print(is_anagram('Eleven plus two','Twelve plus one'))
    print(is_anagram('Eleven plxs two','Twelve plus one'))
    print(is_anagram('cat','tab'))
    print(is_anagram('aa','aa'))
    print(is_anagram('ac','aa'))
    print(is_anagram('a','aa'))
    print(is_anagram('',''))
    print(is_anagram('Nissan','Insane'))
