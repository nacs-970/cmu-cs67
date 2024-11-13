#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# HW07_2
# 204111 Sec 002

# Aomsin
def medal_allocation(list_a:list[int]) -> tuple[list[int], list[int], list[int]]:
    list_a = sorted(list_a,reverse=True)
    list_a = list(filter(lambda x: x != 0,list_a))

    gold = list(filter(lambda x: x == max(list_a),list_a))
    gold_count = len(gold)
    gold_end = list_a[gold_count:]

    silver = list(filter(lambda x: x == max(gold_end),gold_end))
    silver_count = len(silver)
    silver_end = gold_end[silver_count:]

    bronze = list(filter(lambda x: x == max(silver_end),silver_end))

    res = gold,silver,bronze

    if gold_count >= 3:
        return gold,[],[]
    elif gold_count == 2:
        return gold,[],silver
    elif silver_count >= 2:
        return gold,silver,[]

    return gold,silver,bronze

def test():
    assert medal_allocation([9, 8, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7])
    assert medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2]) == ([9], [8], [7, 7])
    assert medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9], [], [8])
    assert medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2]) == ([9, 9, 9, 9], [], [])
    assert medal_allocation([0,0,0,0,0]) == ([],[],[])
    assert medal_allocation([3,2,2,1]) == ([3],[2,2],[])
    assert medal_allocation([1,1,1]) == ([1,1,1],[],[])
    assert medal_allocation([1,0,0]) == ([1],[],[])
    assert medal_allocation([2,1,0,0]) == ([2],[1],[])
    assert medal_allocation([2,2,1,1,1,0,0]) == ([2,2],[],[1,1,1])
    assert medal_allocation([1,2,2,1]) == ([2,2],[],[1,1])

    print("[O m O]")

def random_():
    import random
    for i in range(10):
        l = []
        for i in range(random.randint(3,25)):
            l.append(random.randint(0,10))
        print('in',l)
        print(medal_allocation(l))

if __name__ == "__main__":
    test()
    #random_()
    #print(medal_allocation([2,2,1,1,1,0,0]))
    #print(medal_allocation([9,9,1,8]))
    #print(medal_allocation([2,1,0,0]))
    #print(medal_allocation([1,0,0,0,0]))
    print(medal_allocation([2,2,1,1,1,0]))
    print(medal_allocation([0,0,0,0]))
