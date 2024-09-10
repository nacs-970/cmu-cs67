#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_2
# 204111 Sec 002

def split_and_merge(n:int) -> list[str]:


    def possibility(queue,sequence=[]):
        if not queue:
            list_.append(sequence)
        if queue:
            # the result will same as lecture w11_a_lec1 page 16
            possibility(queue[1:],sequence + [str(queue[0])])
            possibility(queue[1:],sequence)

    possibility(bus)

    bus = range(1,n+1)
    list_ = []
    ans = set()
    base = list_[0]
    print(list_)

    #for poss_add in list_[1:]:
    #    # if poss_add.issubset(temp) or temp.issubset(poss_add)
    #    if set(poss_add) <= set(poss) or set(poss) <= set(poss_add):
    #        continue
    #    if len(poss) + len(poss_add) > n or len(poss) + len(poss_add) < n:
    #        continue
    #    #print(poss,poss_add)
    #    #if len(poss) + len(poss_add) == n:
    #    ans.add(">".join(poss+poss_add))
    return list(ans) , len(ans)
    for poss in list_:

        if len(poss) == n:
            ans.add(">".join(poss))

        else:
            for poss_add in list_[1:]:




        #else:
        #    print(poss)
        #    diff = set(base) - set(poss)
        #    #diff -= set(poss)
        #    #print(diff.union(set(poss)))
        #    ans.add(">".join(diff.union(set(poss))))



if __name__ == "__main__":
    print(split_and_merge(4))
