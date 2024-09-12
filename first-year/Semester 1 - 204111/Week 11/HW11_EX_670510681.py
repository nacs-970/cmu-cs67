#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_EX
# 204111 Sec 002

def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:

    upper_,c = [0],0
    
    for name in name_list[:-1]:
        c += len(name)
        upper_.append(c)

    str_ = list("".join(name_list))
    index_ = rhyme_len - 1
    while len(name_list) != 1:
        #print(name_list)
        #print(index_)
        print(index_,str_[index_],str_)
        if str_[index_] == "_":
            #index_ = index_ + 1 - rhyme_len + str_[index_ - rhyme_len + 1:index_].count("_")
            index_ += 1
            index_ = index_%len(str_)
            continue

        if str_[index_].isupper():
            for i,uindex in enumerate(upper_):
                if index_ == uindex:
                    #print(index_,len(name_list[n]))
                    #print(str_[:index_] + ["_"]*len(name_list[n]) +str_[index_ + len(name_list[n]):])

                    # update str_ with replacing _
                    str_ = str_[:index_] + ["_"]*len(name_list[i]) +str_[index_ + len(name_list[i]):]
                    index_ = index_ + len(name_list[i]) - 1 # update index_ from remove matching name
                    #index_ = index_%len(str_)
                    name_list.pop(i)
                    upper_.pop(i)
                    break

        else:
            str_[index_] = "_"

        #index_ += rhyme_len
        index_ = (index_ + rhyme_len)%(len(str_))


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
    assert eeny_meeny(['John', 'Ann', 'Tom']) == 'John'
    assert eeny_meeny(['Ann', 'Meeneoi']) == 'Ann'
    assert eeny_meeny(['Ann', 'John', 'Meeneoi']) == 'Meeneoi'
    assert eeny_meeny(["Angelica","Ann","Atom"]) == "Angelica"
    assert eeny_meeny(["Atom","Ann"],5) == 'Atom'
    assert eeny_meeny(['Ann', 'John', 'Mee-neoi']) == 'Ann'
    assert eeny_meeny(['John', 'Ann', 'Tom'],5) == 'Tom'
