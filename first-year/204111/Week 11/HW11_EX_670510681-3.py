#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_EX
# 204111 Sec 002
import time

##################
### not finish ###
##################

def update_index(str_,index_,step):
    start = max(0,(index_ - step)+1)
    #print(index_,str_[start:index_+1])
    underscores_count = str_[start:index_ + 1].count("_")
    index_ += underscores_count

    if index_ > len(str_) - 1:
        #index_ = index_ - (len(str_) - 1)
        index_%=len(str_)

    return index_

def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:

    # get all upper character index to dict
    upper_ = list(map(lambda x: len(x),name_list))

    # {index: "name"}
    dict_ = dict(map(lambda x: (sum(upper_[:x]),name_list[x]),range(len(upper_))))

    str_ = list("".join(name_list))
    index_ = rhyme_len - 1

    Debug = False
    looped = False

    while len(name_list) != 1:

        if Debug: print(index_,str_[index_],str_)

        if looped:
            index_ = update_index(str_,index_,rhyme_len)
            if Debug: print('loop',index_,str_[index_],str_)

        if str_[index_].isupper():

            # remove name from name_list
            len_name =  len(dict_[index_])
            name_list.remove(dict_[index_])

            if len(name_list) == 1:
                return name_list[0]

            # update str_
            str_ = str_[:index_] + str_[index_ + len_name:]
            #index_ += 1

            upper_ = list(map(lambda x: len(x),name_list))
            dict_ = dict(map(lambda x: (sum(upper_[:x]),name_list[x]),range(len(upper_))))

        else:
            str_[index_] = "_"
            index_ += 1

        index_ = index_ + (rhyme_len - 1)

        if index_ > len(str_) - 1:
            #print(index_,len(str_))
            index_%=len(str_)
            looped = True

        if Debug: print(index_,str_[index_],str_)

    return name_list[0]

if __name__ == "__main__":
    #print(eeny_meeny(['John', 'Ann', 'Tom']))
    assert eeny_meeny(['John', 'Ann', 'Tom']) == 'John'
    assert eeny_meeny(['Ann', 'Meeneoi']) == 'Ann'
    assert eeny_meeny(['Ann']) == 'Ann'
    assert eeny_meeny(['Ann', 'John', 'Meeneoi']) == 'Meeneoi'
    assert eeny_meeny(['Ann', 'John', 'Mee-neoi']) == 'Ann'
    assert eeny_meeny(["Ann","Atom"]) == 'Ann'
    assert eeny_meeny(["Atom","Ann"],5) == 'Atom'
    assert eeny_meeny(["Angelica","Ann","Atom"]) == "Angelica"
    assert eeny_meeny(['John', 'Ann', 'Tom'],5) == 'Tom'
    print(eeny_meeny(['A','B','C','D'])) 
    x = ['Tomi', 'Maudie', 'Glad', 'Jemima'] # step 9
    print(eeny_meeny(x,9))
