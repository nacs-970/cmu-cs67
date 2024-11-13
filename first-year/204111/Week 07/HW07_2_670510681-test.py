#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# HW07_2
# 204111 Sec 002

# Aomsin
def medal_allocation3(list_a:list[int]) -> tuple[list[int], list[int], list[int]]:
    list_a = sorted(list_a,reverse=True)
    list_a = list(filter(lambda x: x != 0,list_a))

    gold = list(filter(lambda x: x==max(list_a),list_a))
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

def medal_allocation(list_a:list[int]) -> tuple[list[int], list[int], list[int]]:
    list_a.sort(reverse=True) 

    if len(list_a) == 0: return [],[],[] #tuple

    # Gold
    gold_digit = max(list_a) # Max is Gold
    gold_count = list_a.count(gold_digit)
    gold = list(filter(lambda x: x==gold_digit,list_a))
    
    # Silver
    if list_a[-1] == gold_digit: # End with only Gold
        silver = []
        silver_digit = gold_digit
    else:
        silver_digit = list_a[gold_count] # At gold_count is silver_digit
        silver_count = list_a.count(silver_digit)
        silver = list(filter(lambda x: x==silver_digit,list_a))
    
    # Bronze
    if list_a[-1] == silver_digit: # End with only Gold and Silver
        bronze = []
        bronze_digit = silver_digit
    else:
        bronze_digit = list_a[gold_count+silver_count]
        bronze_count = list_a.count(bronze_digit)
        bronze = list(filter(lambda x: x==bronze_digit,list_a))
    
    if bronze_digit == 0: bronze = []
    if silver_digit == 0: silver = []
    if gold_digit == 0: gold = []

    if gold_count >= 3: return gold, [], [] #this is tuple
    if gold_count == 2: return gold, [], silver
    if silver_count >= 2: return gold,silver,[]

    return gold,silver,bronze

def medal_allocation2(list_a: list[int]) -> tuple[list[int], list[int], list[int]]:

    list_a.sort()
    list_a.reverse()

    num1 = list_a.count(max(list_a))
    gold = list([str(max(list_a))]*num1)
    gold = list(map(int, gold))
    if max(list_a) == 0:
        gold = []
    if num1 == len(list_a):
        return (gold,[],[])

    num2 = list_a.count(list_a[num1])
    silver = list([str(list_a[num1])]*num2)
    silver = list(map(int, silver))
    if list_a[num1] == 0:
        silver = []
    if num1+num2 == len(list_a):
        return (gold,silver,[])

    num3 = list_a.count(list_a[num1+num2])
    bronze = list([str(list_a[num1+num2])]*num3)
    bronze = list(map(int, bronze))
    if list_a[num1+num2] == 0:
        bronze = []

    if num1 == 1 and num2 == 1:
        return (gold,silver,bronze)
    elif num1 == 1 and num2 >=2:
        return (gold,silver,[])
    elif num1 == 2:
        return (gold,[],silver)
    elif num1 >= 3:
        return (gold,[],[])

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
        try:
            assert(medal_allocation2(l)) == medal_allocation(l)
        except AssertionError:
            print(l)
            print('Exp :',medal_allocation(l))
            print('Got :',medal_allocation2(l))

if __name__ == "__main__":
    #test()
    random_()
    #print(medal_allocation([2,2,1,1,1,0,0]))
    #print(medal_allocation([9,9,1,8]))
    #print(medal_allocation([2,1,0,0]))
    #print(medal_allocation([1,0,0,0,0]))
    #print(medal_allocation([2,2,1,1,1,0]))
    #print(medal_allocation([0,0,0,0]))
