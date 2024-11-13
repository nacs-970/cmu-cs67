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

    #def power_set(queue,sequence=[]):
    #    if not queue:
    #        set_.append(sequence)
    #    if queue:
    #        # the result will same as lecture w11_a_lec1 page 16
    #        power_set(queue[1:],sequence + [queue[0]])
    #        power_set(queue[1:],sequence)

    # def all_p(queue,sequence=[],list_=[]):
    #     if not queue and sequence not in list_:
    #         list_.append(sequence)
    #     if queue:
    #         # the result will same as lecture w11_a_lec1 page 16
    #         all_p(queue[1:],sequence + [queue[0]])
    #         all_p(queue[:-1],sequence + [queue[-1]])
    #     return list_

    bus = range(1,n+1)
    set_ = power_set(bus)
    l = set()
    top = set_
    bot = top[::-1]
    #all_ = all_p(bus)
    #return all_
    #bus = ['a','b','c']
    #power_set(bus)
    #print(set_)

    # powerset is a way of bus wait in top lane
    # so, reverse it to get bottom lane.
    # and use arrivial sequence from Week 10
    # to match the possibility 
    # tldr; this problem isn't a permutation

    #zip_ = zip(set_,set_[::-1])

    #list_ = list(filter(lambda x: len(x) != 0 and len(x) != n,set_))
    #return list_

    #bot = []

    #for i in top:
    #    #print(i)
    #    bot.append(tuple(filter(lambda x: str(x) not in i,tuple(map(str,bus)))))
    #    #bot = list(filter(lambda x: x not in top,bot))
    #return top
    #bus = range(n,0,-1)
    #bus = ['a','b','c']
    #power_set(bus)
    #bot,list_ = list_,[]

    #top = list(map(str,top))
    #bot = list(map(str,bot))
    #print(top)
    #print(bot)

    def merge(top_l, bot_l,sequence=()):
        #print(sequence)

        if not top_l:
            sequence += bot_l
            l.add(">".join(sequence))
            return

        if not bot_l:
            sequence += top_l
            l.add(">".join(sequence))
            return 
            #return [">".join(sequence)]
        if top_l:
            merge(top_l[1:],bot_l,sequence + (top_l[0],))
        if bot_l:
            merge(top_l,bot_l[1:],sequence + (bot_l[0],))
    
    for i in range(len(top)):
        #print(top[i],bot[i])
        #print(tuple(map(str,bus)))

        #if top[i] + bot[i] == tuple(map(str,bus)):
        #    continue
        #l.add(merge(top[i],bot[i]))
        merge(top[i],bot[i])

    #return l
    #print(l)
    #return f"{time.time() - start:.05f}"
    return list(l)
    #return list(l),f"{(time.time() - start):.07f}"
    # --- #
    # while top and bot:
    #     merge(top[0],bot[0])
    #     top = top[1:]
    #     bot = bot[1:]

    # return set(l)
    # return sorted(set(l)),len(set(l))
    # #print(list(zip(top,bot)))
    # top,bot = list_,list_[::-1]
    # #print(top)
    # #print(bot)

    # def merge(top_,bot_,sequence=[]):
    #     #print(bool(top_),bool(bot_))
    #     if not top_ or not bot_:
    #         #l.append(sequence)
    #         return
    #     fuse = top_[0] + bot_[0]
    #     fuse = list(map(str,fuse))
    #     l.append(">".join(fuse))
    #     merge(top_[1:],bot_[1:])

    # merge(top,bot)
    # return sorted(set(l)), len(set(l))

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
    #split_and_merge(11)
    print(split_and_merge(3))
    print(split_and_merge(4))
    #print(split_and_merge(11))
