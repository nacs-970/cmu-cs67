#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW11_2
# 204111 Sec 002
# TA P'Kla

import time
def split_and_merge(n:int) -> list[str]:

    start = time.time()

    def power_set(queue,sequence=[],list_=[]):

        if not queue:
            list_.append(sequence)

        if queue:
            # the result will same as lecture w11_a_lec1 page 16
            power_set(queue[1:],sequence + [str(queue[0])])
            power_set(queue[1:],sequence)

        return list_

    bus = range(1,n+1); set_ = power_set(bus)

    top = set_; bot = top[::-1]

    # powerset is a way of bus wait in top lane
    # so, reverse it to get bottom lane.
    # and use arrivial sequence from Week 10
    # to match the possibility 
    # tldr; this problem isn't a permutation

    def merge(top_l, bot_l, sequence = [], l = set()):
        #print(sequence)

        if not top_l or not bot_l:
            l.add(">".join(sequence + top_l + bot_l))

        if top_l:
            merge(top_l[1:],bot_l,sequence + [top_l[0]])

        if bot_l:
            merge(top_l,bot_l[1:],sequence + [bot_l[0]])

        return l

    s = set()

    for i in range(len(top)):
        s |= (merge(top[i],bot[i]))
     
    #return f"{time.time() - start:.07f}"
    return sorted(s),f"{time.time() - start:.07f}"
if __name__ == "__main__":
    #split_and_merge(11)
    print(split_and_merge(3))
    print(split_and_merge(4))
    print(split_and_merge(11))