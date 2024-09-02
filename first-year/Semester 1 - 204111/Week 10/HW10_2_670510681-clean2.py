#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW10_2
# 204111 Sec 002

def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str]) -> list[str]:

    def posibility_(first,second,sequence=""):

        #if first == [] and second == []:
        if not(first) and not(second):
            list_.append(sequence[:-1])

        #if first[:1]:
        if first:
            first_id = first[0] + ">"
            posibility_(first[1:],second,sequence + first_id) # first[1:] here to make it not mutable and "sequence + first_id" as the same reason

        #if second[:1]:
        if second:
            second_id = second[0] + ">"
            posibility_(first,second[1:],sequence + second_id)

        #return list_

    l_lane , r_lane = list(l_lane), list(r_lane)
    list_ = []

    #return posibility_(l_lane,r_lane)

    posibility_(l_lane,r_lane)
    return list_

    

if __name__ == "__main__":
    l = 'A','B'
    r = '1','2'
    print(arrival_sequences(l,r))
