#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# Lab11_2
# 204111 Sec 002

def matching_sum(t:tuple[int],target_value:int) -> list[int]:
    if len(t) <= 1:return []

    set_t = set(t)

    for n in set_t:
        if target_value - n in set_t:
            val = target_value - n
            if t.count(val) == 1 and val == n:
                continue
            return [n,val]
    return []

if __name__ == "__main__":
    #print(matching_sum((1,),2))
    #print(matching_sum((1,2,3,5),5))
    assert matching_sum((1,),2) == []
    assert matching_sum((1,),1) == []
    assert matching_sum((1,1),2) == [1,1]
    assert matching_sum((1,2,3,5),5) == [2,3]
    assert matching_sum((1,1,2),4) == []
    assert matching_sum((2,2,2),6) == []

    print(matching_sum((1,),2))
    print(matching_sum((1,),1))
    print(matching_sum((1,1),2))
    print(matching_sum((1,1,2),4))
    print(matching_sum((1,2,2),4))
    print(matching_sum((1,2,3,5),5))
    print(matching_sum((2,2,2),6))
    print(matching_sum((5,2),7))
    print(matching_sum((10,-1,1,-8,3,1),2))
    print(matching_sum((1,2,3,4,-1),1))
    print(matching_sum((1,3,2,5,6,7,1000),1001))
    print(matching_sum((100000000,3,2,5,6,7,1000),100001000))
    #print(matching_sum((1,3,2,5,6,7,1000),100001000))
