#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_EX
# 204111 Sec 002

# didn't use this function
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

    index_ = 0
    marked_index = 0
    debug = False

    while len(name_list) != 1:

        if debug: print("before:",index_,marked_index,str_[index_],str_)
        
        # skip if _
        if str_[index_] == "_":
            index_ += 1

        # if index_ isn't _ and marked_index = to remove (rhyme_len)
        elif marked_index == (rhyme_len - 1):
            if str_[index_].isupper():

                len_name =  len(dict_[index_])
                name_list.remove(dict_[index_])
                str_ = str_[:index_] +  ["_"] * len_name +str_[index_ + len_name:]
                #str_ = str_[:index_] + str_[index_ + len_name:]

                if len(name_list) == 1:
                    return name_list[0]

            else:
                str_[index_] = "_"

            # reset marked_index and continue
            index_ += 1
            marked_index = 0 

        # if index_ isn't _ and marked_index != to remove 
        else:
            index_ += 1
            marked_index += 1

        # hit the end
        if index_ > len(str_) - 1:
            index_ = 0

        if debug: print("after :",index_,marked_index,str_[index_],str_)

    return name_list[0]

if __name__ == "__main__":
    #print(eeny_meeny(['John', 'Ann', 'Tom']))
    assert eeny_meeny(['John', 'Ann', 'Tom']) == 'John'
    assert eeny_meeny(['Ann', 'Meeneoi']) == 'Ann'
    assert eeny_meeny(['Ann']) == 'Ann'

    assert eeny_meeny(['Ann', 'John', 'Meeneoi']) == 'Meeneoi'
    assert eeny_meeny(['Ann', 'John', 'Mee-neoi']) == 'Ann'
    assert eeny_meeny(["Atom","Ann"],5) == 'Atom'
    assert eeny_meeny(['John', 'Ann', 'Tom'],5) == 'Tom'
    assert eeny_meeny(['A','B','C','D']) == 'B'
    x = ['Chiquia', 'Rose', 'Tillie', 'Yettie']
    print(eeny_meeny(x))
    assert eeny_meeny(["Angelica","Ann","Atom"]) == "Angelica"

