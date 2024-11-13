#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW11_2
# 204111 Sec 002
# TA P'Kla

import time
def split_and_merge(n:int) -> list[str]:

    start = time.time()

    def power_set(queue,sequence=()):
        #print(queue,sequence)
        if not queue:
            return [sequence]
            # the result will same as lecture w11_a_lec1 page 16
        non_em = power_set(queue[1:],sequence + (str(queue[0]),))
        em = power_set(queue[1:],sequence)
        return non_em + em

    bus = range(1,n+1)
    set_ = power_set(bus)
    l = set() # using set for memory efficent
    top = set_
    bot = top[::-1]
    
    # edited by myself
    def arrival_sequences(l_lane: tuple[str], r_lane: tuple[str]) -> list[str]:

        list_of_seq = set()

        def generate_seq(l_lane, r_lane, result: list, list_of_seq: list, i=0, j=0):
            if i == len(l_lane) and j == len(r_lane):
                list_of_seq.add('>'.join(result))
            if i < len(l_lane):
                generate_seq(l_lane, r_lane, result + [l_lane[i]], list_of_seq,  i + 1, j)
            if j < len(r_lane):
                generate_seq(l_lane, r_lane, result + [r_lane[j]], list_of_seq, i, j + 1)    
        
        generate_seq(l_lane, r_lane, [], list_of_seq)
        return list_of_seq
    
    for i in range(len(top)):
        l |= (arrival_sequences(top[i],bot[i]))

    return sorted(l)

if __name__ == "__main__":
    #split_and_merge(11)
    print(split_and_merge(3))
    print(split_and_merge(4))
    #print(split_and_merge(11))
