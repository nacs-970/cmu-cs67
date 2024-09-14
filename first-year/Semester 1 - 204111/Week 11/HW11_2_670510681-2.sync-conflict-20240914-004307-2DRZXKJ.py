#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_2
# 204111 Sec 002
# TA P'Kla

def split_and_merge(n:int) -> list[str]:

    def power_set(queue,sequence=[]):
        #print(queue,sequence)
        if not queue:
            set_.append(sequence)
        if queue:
            # the result will same as lecture w11_a_lec1 page 16
            power_set(queue[1:],sequence + [queue[0]])
            power_set(queue[1:],sequence)

    set_,l = [],[]
    bus = tuple(range(1,n+1))
    #bus = ['a','b','c']
    power_set(bus)
    return set_
    # powerset is a way of bus wait in top lane
    # so, reverse it to get bottom lane.
    # and use arrivial sequence from Week 10
    # to match the possibility 
    # tldr; this problem isn't a permutation
    top = set_
    #bus = range(n,0,-1)
    #bus = ['a','b','c']
    #power_set(bus)
    #bot,list_ = list_,[]
    bot = top[::-1]

    #top = list(map(str,top))
    #bot = list(map(str,bot))
    #print(top)
    #print(bot)

    def merge(top_l, bot_l,sequence=[]):
        if not top_l and not bot_l:
            sequence = list(map(str,sequence))
            l.append(">".join(sequence))
        if top_l:
            merge(top_l[1:],bot_l,sequence + [top_l[0]])
        if bot_l:
            merge(top_l,bot_l[1:],sequence + [bot_l[0]])

    for i in zip(top,bot):
        merge(i[0],i[1])

    return sorted(set(l))
    return sorted(set(l)),len(set(l))
    #print(list(zip(top,bot)))
    top,bot = list_,list_[::-1]
    #print(top)
    #print(bot)

    def merge(top_,bot_,sequence=[]):
        #print(bool(top_),bool(bot_))
        if not top_ or not bot_:
            #l.append(sequence)
            return
        fuse = top_[0] + bot_[0]
        fuse = list(map(str,fuse))
        l.append(">".join(fuse))
        merge(top_[1:],bot_[1:])

    merge(top,bot)
    return sorted(set(l)), len(set(l))

    #while top and bot:
    #    fuse = top[0] + bot[0]
    #    fuse = list(map(str,fuse))
    #    l.append(">".join(fuse))
    #    top = top[1:]
    #    bot = bot[1:]
    #return list(set(l)), len(set(l))
    #def merge(top,bot):
#['1>2>3>4', '1>2>4>3', '1>3>2>4', '1>3>4>2', '1>4>2>3', '2>1>3>4', '2>1>4>3', '2>3>1>4', '2>3>4>1', '2>4>1>3', '3>1>2>4', '3>1>4>2', '3>4>1>2', '4>1>2>3'] 
if __name__ == "__main__":
    print(split_and_merge(11))
