#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_EX
# 204111 Sec 002

##################
### not finish ###
##################

def update_index(str_,index_,step):
    start = max(0,index_ - step)
    underscores_count = str_[start:index_+1].count("_")
    index_ += underscores_count

    if index_ > len(str_) - 1:
        #index_ = index_ - (len(str_) - 1)
        index_%=len(str_)
    #print(index_ - underscores_count)
    #print("update")
    return index_

Debug = True
def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:
    
    # get all upper character index to dict
    upper_ = list(map(lambda x: len(x),name_list))

    # {index: "name"}
    dict_ = dict(map(lambda x: (sum(upper_[:x]),name_list[x]),range(len(upper_))))
    str_ = list("".join(name_list))

    #index_ = -1
    index_ = rhyme_len - 1
    looped = False

    while len(name_list) != 1:
        
        break_check = str_
        if Debug:print(index_,str_[index_],str_)
        #print(str_)
        
        if looped:
            index_ = update_index(str_,index_,rhyme_len)
                
        #if str_[index_] == "_":
        #    index_ = update_index(str_,index_,rhyme_len)
            #start = max(0,index_ - rhyme_len)
            #underscores_count = str_[start:index_+1].count("_")
            #index_ += underscores_count

            #if index_ > len(str_) - 1:
            #    index_ = index_ - len(str_) - 1
            #continue

        if str_[index_].isupper():

            # remove name from name_list
            len_name =  len(dict_[index_])
            name_list.remove(dict_[index_])

            if len(name_list) == 1:
                return name_list[0]

            # update str_
            str_ = str_[:index_] + str_[index_ + len_name:]
            index_ -= 1
            #index_ = (index_ + len_name)
            #print(index_)
            #if index_ > len(str_) - 1:
            #    index_ = index_ - len(str_) - 1
            #    print(index_,"remove")

            #index_ %= len(str_)

            # update dict
            upper_ = list(map(lambda x: len(x),name_list))
            dict_ = dict(map(lambda x: (sum(upper_[:x]),name_list[x]),range(len(upper_))))

        else:
            str_[index_] = "_"

        index_ = index_ + rhyme_len

        if index_ > len(str_) - 1:
            #print(index_,len(str_))
            index_%=len(str_)
            #index_ = index_ - (len(str_) - 1)
            looped = true
        print(str_)
        if break_check == str_:
            return "break"
        #index_ = update_index(str_,index_,rhyme_len)

        #index_ = (index_ + rhyme_len)%len(str_)
        #print(index_)
        if Debug: print(index_,str_[index_],str_)

    #print(name_list[0])
    return name_list[0]

if __name__ == "__main__":
    #eeny_meeny(['John', 'Ann', 'Tom'])
    assert eeny_meeny(['John', 'Ann', 'Tom']) == 'John'
    assert eeny_meeny(['Ann', 'Meeneoi']) == 'Ann'
    assert eeny_meeny(['Ann']) == 'Ann'
    assert eeny_meeny(['Ann', 'John', 'Meeneoi']) == 'Meeneoi'
    assert eeny_meeny(['Ann', 'John', 'Mee-neoi']) == 'Ann'
    assert eeny_meeny(["Atom","Ann"],5) == 'Atom'
    assert eeny_meeny(['John', 'Ann', 'Tom'],5) == 'Tom'
    assert eeny_meeny(["Angelica","Ann","Atom"]) == "Angelica"
    assert eeny_meeny(['A','B','C','D']) == 'B'
    print(eeny_meeny(['Chiquia', 'Rose', 'Tillie', 'Yettie']))
    print(eeny_meeny(['Arabelle', 'Philipa', 'Martina', 'Marcy', 'Lonna', 'Joyce', 'Jobyna', 'Cybil'])) # step 4
    #print(eeny_meeny(['Tonya', 'Rubi', 'Stephani', 'Min', 'Grier', 'Lotte', 'Kamillah', 'Pammy', 'Fara', 'Susannah'])) # step 7
    x = ['Siouxie', 'Harriet', 'Bernete', 'Chris', 'Romy', 'Bree', 'Odelia'] # step 6
    print(eeny_meeny(x,6))
