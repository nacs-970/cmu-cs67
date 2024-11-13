#!/usr/bin/env python
# 670510681
# Atithep Thepkij (Tun)
# HW13_EX
# 204111 Sec 002
# [9,12,6]
#00       
#01                                 |>>~ 
#02                                 | 
#03                               /^^^\ 
#04                              /     \ 
#05                             /^^^^^^^\ 
#06         /^^^\              /         \ 
#07        /     \            /           \ 
#08       /^^^^^^^\          /             \ 
#09      /         \        /               \        /^^^\ 
#10     /           \      /                 \      /     \ 
#11    /             \    /                   \    /^^^^^^^\ 
#12   /               \  /                     \  /         \ 
#13  /                 \/                       \/           \ 
#14 /::::::::::::::::::/::::::::::::::::::::::::/:::::::::::::\

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
    towers = []
    for mountain_h in list_a:

        temp = []

        for height in range(max_):
            if height >= mountain_h:
                temp.append(" " * (max_ - height) + " ")

            else:
                if height in [0,2]: # top
                    temp.append(" "*(max_ - height) + "/" + "^"*(3 + (2 * height)) + "\\")

                elif height == mountain_h - 1: # bottom
                    temp.append(" " * (max_ - height) + "/" + ":" * (3 + (2 * height)) + "\\")

                else:
                    temp.append(" " * (max_ - height) + "/" + " " * (3 + (2 * height)) + "\\")

        towers.append(temp)

    result = []
    for i in towers:
        print("\n".join(i))
    return 0
    for i in range(max_):
        line = []
        for tower in towers:
            line.append(tower[i])
        result.append("".join(line))

if __name__ == "__main__":
    sand_towers([9,12,6])
    #sand_towers([4,4,4])

