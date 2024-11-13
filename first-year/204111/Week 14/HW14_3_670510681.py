#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW14_3
# 204111 Sec 002

def radix_word(list_x: list[str],show_steps=False):

    # read lecture Sorting & Searching
    import string
    max_ = max(list(map(len,list_x)))
    list_ = list(map(lambda x: x + " "*(max_-len(x)), list_x))

    # LSD
    for i in range(-1,-(max_+1),-1):

        # move string to the left
        dict_ = dict(map(lambda x: (str(x),[])," " + string.ascii_letters))
        #dict_ = dict(map(lambda x: (str(x),[])," " + string.ascii_lowercase))
        
        # sorting
        for j in list_:
            dict_[j[i]] += [j]
        list_ = [n for values in dict_ for n in dict_.get(values)]

        if show_steps:
            print([x.strip() for x in list_])

    list_x[:] = [x.strip() for x in list_]

    #return list(map(str.strip,list_))
if __name__ == "__main__":
    #list_x = ['beer', 'wine', 'vinegar', 'vodka']
    list_x = ['bat','ant','beer','rum','wine','candy']
    radix_word(list_x,True)
    print("---")
    print(list_x)
