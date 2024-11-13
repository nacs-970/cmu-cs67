#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# HW07_2
# 204111 Sec 002


def medal_allocation(list_a:list[int]) -> tuple[list[int], list[int], list[int]]:
    # Can't use Destrutive but for some reason add isdigit make it functional
    list_a = list(filter(lambda x: str(x).isdigit(),list_a)) # Because it's Destrutive
    list_a.sort(reverse=True)
    
    # don't Destrutive 100/100
    #list_a = sorted(list_a,reverse=True)


    #if len(list_a) == 0: return tuple([[]])+tuple([[]])+tuple([[]]) 
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

    #if gold_count >= 3: return tuple([gold]) + tuple([[]]) + tuple([[]])
    #if gold_count == 2: return tuple([gold]) + tuple([[]]) + tuple([silver])
    #if silver_count >= 2: return tuple([gold]) + tuple([silver]) + tuple([[]])

    #return tuple([gold]) + tuple([silver]) + tuple([bronze])

    if gold_count >= 3: return gold, [], [] #this is tuple
    if gold_count == 2: return gold, [], silver
    if silver_count >= 2: return gold,silver,[]

    return gold,silver,bronze

    #print(gold,silver,bronze)
    #print(gold_digit,silver_digit,bronze_digit)

#    return print(bronze)
#    # Gold start fist 
#    gold_digit = max(list_a)
#    if gold_digit == 0:
#        gold,silver,bronze = [],[],[]
#    gold_count = list_a.count(gold_digit)
#    len_check += gold_count
#
#    if len_check == len_:
#        gold = list_a,silver = [], bronze = []
#    gold = list_a[:gold_count]
#
#    # Silver start behind gold
#    silver_digit = list_a[gold_count]
#    silver_count = list_a.count(silver_digit)
#    silver = list_a[gold_count:gold_count+silver_count]
#
#    # bronze start behind gold+silver
#    bronze_digit = list_a[gold_count+silver_count]
#    bronze_count = list_a.count(bronze_digit)
#    bronze = list_a[gold_count+silver_count:gold_count+silver_count+bronze_count]

#    def allocator(g,s,b):
#        len_g = len(g)
#        len_s = len(s)
#        len_b = len(b)
#        bronze_digit_local = bronze_digit
#
#        if len_g >= 3:
#            len_s,len_b = 0,0
#            s,b = [],[]
#
#        if len_g == 2:
#            len_b = len_s
#            len_s = 0
#            b = s 
#            bronze_digit_local = silver_digit # local focus bronze
#            s = []
#
#        if len_s >= 2:
#            len_b = 0
#            b = []
#
#        if bronze_digit_local == 0:
#            b = []
#        if silver_digit == 0:
#            s = []
#        if gold_digit == 0:
#            g,s,b = [],[],[]
#        return tuple([g]) + tuple([s]) + tuple([b])
        
    #print(allocator(gold,silver,bronze))
    #return allocator(gold,silver,bronze)
    #return tuple([gold]) + tuple([silver]) + tuple([bronze])

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
