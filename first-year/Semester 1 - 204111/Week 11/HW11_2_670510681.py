#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# HW11_2
# 204111 Sec 002

def split_and_merge(n:int) -> list[str]:

    def power_set(queue,sequence=[]):
        #print(queue,sequence)
        if not queue:
            list_.append(sequence)
        if queue:
            #if sequence:
            #    possibility(queue[1:],[str(queue[0])] )
            #    possibility(queue[1:],sequence)

            # the result will same as lecture w11_a_lec1 page 16
            power_set(queue[1:],sequence + [queue[0]])
            power_set(queue[1:],sequence)

            #possibility(queue[1:],sequence + [str(queue[0])])
            #possibility(queue[1:],[str(queue[0])] + sequence)
            #possibility(queue[:-1],sequence + [str(queue[-1])])
            #possibility(queue[:-1],[str(queue[-1])] + sequence)

    list_,l = [],[]
    bus = range(1,n+1)
    power_set(bus)
    return list_
    list_2 = list(map(lambda x: x[::-1] if x[-1:] != [n] else x,list_))
    #print(list_,list_2)

    list_ = list_ + list_2
    base = list(map(str,list_[0]))

    #l = list(map(lambda x: list(map(lambda y: x + [y] if y not in x else [],base)),list_))
    for i in list_:
        t = list(map(str,i))
        #t = list(map(lambda x: t + [x] if x not in t else [],base))
        for j in base:
            #print(t)
            if j not in t:
                t = t + [j]
        l.append(">".join(t))
        t = list(map(str,i))
        if t != [str(n)] and t != []:
            for j in base[::-1]:
                if j not in t:
                    t = t + [j]
            l.append(">".join(t))

    #return list_  
    return sorted(set(l)),len(sorted(set(l)))
    return sorted(list(set(l))) #,list_

    #ans = set()
    #base = list_[0]

    #for poss_add in list_[1:]:
    #    # if poss_add.issubset(temp) or temp.issubset(poss_add)
    #    if set(poss_add) <= set(poss) or set(poss) <= set(poss_add):
    #        continue
    #    if len(poss) + len(poss_add) > n or len(poss) + len(poss_add) < n:
    #        continue
    #    #print(poss,poss_add)
    #    #if len(poss) + len(poss_add) == n:
    #    ans.add(">".join(poss+poss_add))
    #return list(ans) , len(ans)
    #for poss in list_:

    #    if len(poss) == n:
    #        ans.add(">".join(poss))

    #    else:
    #        for poss_add in list_[1:]:




        #else:
        #    print(poss)
        #    diff = set(base) - set(poss)
        #    #diff -= set(poss)
        #    #print(diff.union(set(poss)))
        #    ans.add(">".join(diff.union(set(poss))))



if __name__ == "__main__":
    print(split_and_merge(4))
