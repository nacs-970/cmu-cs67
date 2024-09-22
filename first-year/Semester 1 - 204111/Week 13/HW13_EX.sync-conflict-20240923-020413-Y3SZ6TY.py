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
    space_l = []
    for i in list_a:
        if i == max_:
            t = [" "*(i+1) + "|>>~" + " "*(i-4), " "*(i+1) + "|" + " "*(3 + (i-4))]
        else:
            t = []
        #t = []
        for index in range(i):
            space = (i - index - 1)
            char = " "

            if index == i-1:
                str_ = ["/" + ":"*(2 + (2*index))]
                t += str_
                continue

            if index == 0 or index == 2:
                char = "^"
            if index == i - 2:
                str_ = [" "* (space-1) + "/" + char*(3 + (2*index)) + "\\" + " "* (space-2)]
            else:
                str_ = [" "* (space) + "/" + char*(3 + (2*index)) + "\\" + " "* (space-2)]
            t += str_
        #t = "\n".join(t)
        #print("\n".join(t))
        split_ += [t]

    max_ = max([len(x) for x in split_])
    diff_ = list(map(lambda x:  max_ - len(x),split_))
    split_ = list(map(lambda x:  ( [(" ")*(2*len(x) + 1)] * (max_ - len(x))) + x ,split_))
    ans = [""]

    for index in range(max_):
        temp = []
        for row in range(len(split_)):
            temp += [split_[row][index]]
            #print(split_[j][i])
        #print("".join(temp))
        if index == max_ - 2:
            temp = [" "] + temp
        ans += ["".join(temp)]

    ans[-1] += ":\\"
    ans = list(map(str.rstrip,ans))
    #print("\n".join(ans))
    return "\n".join(ans)
if __name__ == "__main__":
    sand_towers([9,12,6])
    sand_towers([4,4,4])
    #sand_towers([5,5,5])
    sand_towers([7])
