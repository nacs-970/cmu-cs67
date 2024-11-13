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
        # max - min now work at the moment
        #if now > list_[index_-1]:
        #    pass
        #    list_[index_],list_[index_-1] = list_[index_-1],list_[index_]

        # min - max
        if now < list_[index_-1]:
            list_[index_-1],list_[index_] = list_[index_],list_[index_-1]

        return sort_str(list_,index_-1)


    s1_sort = sort_str(s1,len_s1)
    s2_sort = sort_str(s2,len_s2)

    # Remove dupe
    #range_s1 = range(len(s1_sort))
    #range_s2 = range(len(s2_sort))

    #def remove_dupe(list_,index_):
    #    letter = list_[index_]
    #    count_ = list_.count(letter)
    #    
    #    # Have dupe
    #    if count_ > 1: return list_[index_+count_-1]
    #    else: return list_[index_]

    #s1_nodupe = list(map(lambda x: remove_dupe(s1_sort,x),range_s1))
    #return s1_nodupe

    len_s1 = len(s1)-1
    len_s2 = len(s2)-1
    
    range_s1 = range(len(s1_sort)-1)
    range_s2 = range(len(s2_sort)-1)
    
    def remove_dupe(list_,index_):
        if index_ == 0: return list_
        letter = list_[index_]
        count_ = list_.count(letter)
        
        # Have dupe
        if count_ > 1:
            list_.pop(index_)
            #list_ = list_[:count_-1] + list_[count_+1:]
            index_ = len(list_)
        #print(list_)
        return remove_dupe(list_,index_-1)

    s1_nodupe = remove_dupe(s1_sort,len_s1) # one letter per each
    s2_nodupe = remove_dupe(s2_sort,len_s2)

    #len_s1 = len(s1_nodupe)
    #len_s2 = len(s2_nodupe)
    #if len_s1 > len_s2:max_,min_ = s1_nodupe,s2_nodupe
    #elif len_s1 < len_s2:max_,min_ = s2_nodupe,s1_nodupe
    #else:max_,min_ = s1_nodupe,s2_nodupe

    # Have less or more character
    max_,min_ = max(s1_nodupe,s2_nodupe),min(s1_nodupe,s2_nodupe)

    range_min = range(len(min_))
    range_max = range(len(max_))
    
    compare_min = list(map(lambda x: min_[x] in max_,range_min))
    compare_max = list(map(lambda x: max_[x] in min_,range_max))
    if False in compare_min or False in compare_max: return False
    
    # Character count if s1 and s2 has equal character
    len_count = len(s1_nodupe)-1
    range_ = range(len(s1_nodupe))
    
    count_s1 = list(map(lambda x: s1_b.lower().count(s1_nodupe[x]),range_))
    count_s2 = list(map(lambda x: s2_b.lower().count(s2_nodupe[x]),range_))
    character_count = list(map(lambda x: count_s1[x] == count_s2[x],range_))

    if False in character_count:return False
    else:return True


    #s1_nodupe = list(map(lambda x: s1_sort[x] if s1_sort[x] != s1_sort[x+1] else s1_sort[x+1],range_s1))
    #s1_nodupe = list(filter(lambda x: x != 0,s1_nodupe))

    #s2_nodupe = list(map(lambda x: s2_sort[x] if s2_sort[x] != s2_sort[x+1] else 0,range_s2))
    #s2_nodupe = list(filter(lambda x: x != 0,s2_nodupe))



    #return s1_sort,s1_nodupe
    #str_ = list(filter(lambda x: s1[x] != s1[x],range_))

if __name__ == "__main__":
    print(is_anagram('Eleven plus two','Twelve plus one'))
    print(is_anagram('Eleven plxs two','Twelve plus one'))
    print(is_anagram('cat','tab'))
    print(is_anagram('aa','aa'))
    print(is_anagram('ac','aa'))
    print(is_anagram('a','aa'))
    print(is_anagram('',''))
    print(is_anagram('Nissan','Insane'))
