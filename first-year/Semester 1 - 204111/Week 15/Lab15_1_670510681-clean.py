#!/usr/bin/env python
# Atithep Thepkij
# 670510681
# Lab15_1
# 204111 Sec 002

def sum_nested_list(list_a: list,depth=1):

    if not list_a:
        return 0
    
    # categorize list
    list_of_list = list(filter(lambda x:isinstance(x,list),list_a))
    list_ = list(filter(lambda x:not isinstance(x,list),list_a))
    
    now = sum(map(lambda x: x*depth, list_))
    next_ = sum(sum_nested_list(sub_l,depth + 1) for sub_l in list_of_list)
    # for each iteration it gonna recursion isolated

    #print(next_)
    return now + next_


if __name__ == "__main__":
    print(sum_nested_list([1, 2, [[3, [[4], 5]], [6, 7]]]))
    print(sum_nested_list([1, 2, [[3, 0], 4], 8]))
    print(sum_nested_list([9, [[8, [7]], 6, [5, [44, [33]]]]]))
