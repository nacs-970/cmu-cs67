#!/usr/bin/env python
# 670510681
# Atithep Thepkij (Tun)
# HW13_EX
# 204111 Sec 002
# [9,12,6]
#     
#                                |>>~ 
#                                | 
#                              /^^^\ 
#                             /     \ 
#                            /^^^^^^^\ 
#        /^^^\              /         \ 
#       /     \            /           \ 
#      /^^^^^^^\          /             \ 
#     /         \        /               \        /^^^\ 
#    /           \      /                 \      /     \ 
#   /             \    /                   \    /^^^^^^^\ 
#  /               \  /                     \  /         \ 
# /                 \/                       \/           \ 
#/::::::::::::::::::/::::::::::::::::::::::::/:::::::::::::\
# 58

# 7
# 
#        |>>~ 
#        | 
#      /^^^\ 
#     /     \ 
#    /^^^^^^^\ 
#   /         \ 
#  /           \ 
# /             \ 
#/:::::::::::::::\ 

def sand_towers(list_a: list[int]) -> str:
    max_ = max(list_a)
    total_width = 0
    split_ = []
    list_ = [[""]]
    for i in list_a:
        if i == max_:
            t = [" "*(i+1) + "|>>~", " "*(i+1) + "|"]
        else:
            t = []
        for index in range(i):
            str_ = []
            space = (i - index - 1)
            #index = (i-1) - j
            if index == 0 or index == 2:
                str_ += [" "* space + "/" + "^"*(3 + (2*index)) + "\\"]
            elif index == i-1:
                str_ += [" "* space + "/" + ":"*(3 + (2*index)) + "\\"]
                total_width += len(" "* space + "/" + ":"*(3 + (2*index)) + "\\")
            else:
                str_ += [" "* space + "/" + " "*(3 + (2*index)) + "\\"]
            t += str_
        #print("\n".join(t))
        #t = "\n".join(t)
        split_ += [t]
    ans = []
    print(total_width)
    max_ = max([len(x) for x in split_])
    diff_ = list(map(lambda x:  max_ - len(x),split_))
    split_ = list(map(lambda x:  ( [""] * (max_ - len(x))) + x ,split_))
    #print(split_)
if __name__ == "__main__":
    sand_towers([9,12,6])
    #sand_towers([4,4,4])

