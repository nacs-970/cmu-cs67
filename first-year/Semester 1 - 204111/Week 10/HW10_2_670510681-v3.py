#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW10_2
# 204111 Sec 002

def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str], sequence=()):
    #if not l_lane and not r_lane:
    #    list_.append(sequence[:-1])
    #print(sequence)
    if not l_lane:
        sequence += r_lane
        return [">".join(sequence)]
    if not r_lane:
        sequence += l_lane
        return [">".join(sequence)]

    l_first = arrival_sequences(l_lane[1:], r_lane, sequence + (l_lane[0],))
    r_first = arrival_sequences(l_lane, r_lane[1:], sequence + (r_lane[0],))
    return l_first + r_first 

if __name__ == "__main__":
    n = 3
    l = tuple(map(str,range(1,n+1)))
    r = tuple(map(str,range(n,0,-1)))
    #l = 'A','B','C'
    #r = '1','2','3'
    print(arrival_sequences(l,r))
