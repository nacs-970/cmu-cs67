#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_2
# 204111 Sec 002
# TA P'Kla
# not finish

def split_and_merge(n:int) -> list[str]:

    #def power_set(queue,sequence=[]):
    #    if not queue:
    #        set_.append(sequence)
    #    if queue:
    #        # the result will same as lecture w11_a_lec1 page 16
    #        power_set(queue[1:],sequence + [queue[0]])
    #        power_set(queue[1:],sequence)

    set_ = [[]]; bus = range(1,n+1); l = set()

    # alternative way of makeing power_set

    for i in bus:
        q = map(lambda x: x + [i],set_.copy())
        set_ += q

    set_ = set_[1:-1]
    #set_r = set_[::-1] 
    top,bot=[],[] 

    # filter dupe bus
    #while set_:
    #    #print(set_r)
    #    if set_[0] + set_r[0] != bus:
    #        top += [set_[0]]
    #        bot += [set_r[0]]

    #    set_ = set_[1:]
    #    set_r = set_r[1:]

    #return top,bot
    #power_set(bus)

    # powerset is a way of bus wait in top lane
    # so, reverse it to get bottom lane.
    # and use arrivial sequence from Week 10
    # to match the possibility 
    # tldr; this problem isn't a permutation

    top = set_;bot = top[::-1]

    def merge(t,b):

        ans = set() 

        def merge_2(top_l,bot_l,sequence=""):
            if not top_l and not bot_l:
                ans.add(sequence[:-1])

            if top_l:
                merge_2(top_l[1:],bot_l,sequence + str(top_l[0]) + ">")

            if bot_l:
                merge_2(top_l,bot_l[1:],sequence + str(bot_l[0]) + ">")

        merge_2(t,b)

        return ans

    while top or bot:
        l |= merge(top[0],bot[0])
        top = top[1:]
        bot = bot[1:]

    return sorted(l)
    return sorted(set(l)),len(set(l))

if __name__ == "__main__":
    print(split_and_merge(3))
    print(split_and_merge(4))
    print(split_and_merge(11))
