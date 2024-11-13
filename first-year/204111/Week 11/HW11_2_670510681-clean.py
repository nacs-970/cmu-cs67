#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_2
# 204111 Sec 002
# TA P'Kla
# not finish
def split_and_merge(n:int) -> list[str]:

    def power_set(queue,sequence=[]):
        if not queue:
            set_.append(sequence)
        if queue:
            # the result will same as lecture w11_a_lec1 page 16
            power_set(queue[1:],sequence + [queue[0]])
            power_set(queue[1:],sequence)

    set_,l = [],[]
    bus = range(1,n+1)
    power_set(bus)

    # powerset is a way of bus wait in top lane
    # so, reverse it to get bottom lane.
    # and use arrivial sequence from Week 10
    # to match the possibility 
    # tldr; this problem isn't a permutation

    top = set_;bot = top[::-1]

    def merge(top_l, bot_l,sequence=[]):
        if not top_l and not bot_l:
            sequence = list(map(str,sequence))
            l.append(">".join(sequence))
        if top_l:
            merge(top_l[1:],bot_l,sequence + [top_l[0]])
        if bot_l:
            merge(top_l,bot_l[1:],sequence + [bot_l[0]])

    while top and bot:
        merge(top[0],bot[0])
        top = top[1:]
        bot = bot[1:]

    return sorted(set(l))
    return sorted(set(l)),len(set(l))

if __name__ == "__main__":
    print(split_and_merge(11))
