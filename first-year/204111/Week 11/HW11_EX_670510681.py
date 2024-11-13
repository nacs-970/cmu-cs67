#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_EX
# 204111 Sec 002
import time

##################
### not finish ###
##################

def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:

    start = time.time()

    #name_list = list(filter(lambda x: len(x) > 0,name_list))
    #if not name_list:
    #    return ""
    #name_list = list(filter(lambda x: x[0].isupper,name_list))

    # get all upper index
    upper_ = list(map(lambda x: len(x),name_list))
    upper_ = list(map(lambda x: sum(upper_[:x]),range(len(upper_))))
    #upper_ = [0] + upper_
    #print(upper_)

    looped = False
    str_ = list("".join(name_list))
    index_ = rhyme_len - 1

    #if not (list(filter(str.isupper,str_))) :
    #    return ""

    while len(name_list) != 1:
        #print(name_list)
        #print(index_)
        #print(len(str_),index_,str_[index_],str_)

        #print(str_[u_stop:index_])
        if str_[index_] == "_":
            #print("hit")
            u_stop = max(0,index_ - rhyme_len - 1)
            u_count = str_[u_stop:index_+1].count("_")
            index_ += u_count
            index_ %= len(str_)

            #print(index_,str_[index_],str_[:index_+1] )#+ str_[index_:])
            #index_next = index_ + 1 - rhyme_len + str_[index_ - rhyme_len + 1:index_].count("_")
            #index_ += u_count
            #index_ += str_[:index_+1].count("_")
            #index_ = index_%len(str_)
            #print(index_,str_[index_],str_)
            continue

        if str_[index_].isupper():

            for i,uindex in enumerate(upper_):
                if index_ == uindex:
                    #print(index_,len(name_list[n]))
                    #print(str_[:index_] + ["_"]*len(name_list[n]) +str_[index_ + len(name_list[n]):])

                    # update str_ with replacing _
                    #str_ = str_[:index_] + ["_"]*len(name_list[i]) +str_[index_ + len(name_list[i]):]
                    str_ = str_[:index_] + str_[index_ + len(name_list[i]):]
                    #print(str_)
                    index_ = index_ + len(name_list[i]) - 1 # update index_ from remove matching name
                    index_ = (index_ + rhyme_len)%(len(str_))
                    #index_ -= 1 # update index_ from remove matching name
                    #index_ %= len(str_)
                    #print(index_)
                    name_list.pop(i)
                    upper_.pop(i)

                    if len(name_list) == 1:
                        return name_list[0]

                    upper_ = list(map(lambda x: len(x),name_list))
                    upper_ = list(map(lambda x: sum(upper_[:x]),range(len(upper_))))
                    break

        else:

            #str_ = str_[:index_] + ["_"] + str_[index_:]
            str_[index_] = "_"
            #if looped:
            #    index_ += str_[:index_].count("_")
            #    index_ = index_%len(str_)

                #if str_[index_].islower():
                #    str_[index_] = "_"

                #else:
                #    for i,uindex in enumerate(upper_):
                #        if index_ != uindex:
                #            continue
                #        if index_ == uindex:
                #            str_ = str_[:index_] + str_[index_ + len(name_list[i]):]
                #            #index_ = index_ - len(name_list[i]) - 1 # update index_ from remove matching name
                #            index_ -= 1 # update index_ from remove matching name
                #            name_list.pop(i)
                #            upper_.pop(i)

                #            if len(name_list) == 1:
                #                return name_list[0]

                #            upper_ = list(map(lambda x: len(x),name_list))
                #            upper_ = list(map(lambda x: sum(upper_[:x]),range(len(upper_))))
                #            break

            #index_ += 1

        #index_ += rhyme_len
        index_ = (index_ + rhyme_len)%(len(str_))

        #print(len(str_),index_,str_[index_],str_)
        #print(index_next)
    #print(f"{time.time() - start:.07f}")

    return name_list[0]

            #while name not in name_list:
            #    if not n or n[0].:
            #        break
            #    if n[0].islower():
            #        name += n[0]
            #        n = n[1:]
            #print(name)
            #name = ""
            #while name not in name_list:
            #    name += str_[n]
            #    n += 1
            #print(str_[index_]+str_[index_+1])

            #for name in name_list:
            #    if name.startswith(str_[index_]):
            #        break
            #    else:
            #        name = ""

            #print(name)
            #name_list.remove(name)
            #str_ = "".join(str_).replace(name,"")
            #str_ = list(str_)


        #if start > len(str_):
        #    start = start - len(str_)
        #print(str_)
        #print(start,remove_list)
        
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

