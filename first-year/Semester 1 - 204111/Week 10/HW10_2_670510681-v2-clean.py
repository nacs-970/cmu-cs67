#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW10_2
# 204111 Sec 002

def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str],sequence="",list_=[]) -> list[str]:
    print(list_)
    l_lane , r_lane = list(l_lane), list(r_lane)
    if not l_lane and not r_lane:
        list_.append(sequence[:-1])
    if l_lane:
        arrival_sequences(l_lane[1:],r_lane,sequence + l_lane[0] + ">")
    if r_lane:
        arrival_sequences(l_lane,r_lane[1:],sequence + r_lane[0] + ">")

    return list_

if __name__ == "__main__":
    l = 'A','B','C'
    r = '1','2','3'
    print(arrival_sequences(l,r))
