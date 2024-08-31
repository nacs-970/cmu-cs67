#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW09_2
# 204111 Sec 002
def median_of_median(list_a: list[float]) -> float:

    def median(list_):
        len_ = len(list_)
        mid = len_//2
        if len_%2 == 1: return list_[mid]
        return (list_[mid] + list_[mid-1])/2

    if len(list_a) == 3: 
        min_ = min(list_a)
        max_ = max(list_a)
        mid_ = sum(list_a)-min_-max_
        return float(median([min_,mid_,max_]))

    if len(list_a) <= 2:
        return float(median(list_a))

    step = len(list_a)//3
    step_a,step_b = step,2*step
    
    list_1 = list_a[:step_a]
    list_2 = list_a[step_a:step_b]
    list_3 = list_a[step_b:] # remainder will got medianed

    list_1 = median_of_median(list_1)
    list_2 = median_of_median(list_2)
    list_3 = median_of_median(list_3)
    #print(list_1,list_2,list_3)
    return median_of_median([list_1,list_2,list_3]) # find median

def median_of_median2(list_a):
    def median(list_):
        len_ = len(list_)
        mid = len_//2
        if len_%2 == 1: return list_[mid]
        return (list_[mid] + list_[mid-1])/2
        
    if len(list_a) == 3: 
        min_ = min(list_a)
        max_ = max(list_a)
        mid_ = sum(list_a)-min_-max_
        return float(median([min_,mid_,max_]))

    if len(list_a) <= 2:
        return float(median(list_a))
    
    front = list_a[:3]
    back = list_a[3:]
    list_ = [median_of_median2(front)] + back
    return median_of_median2(list_)

def test():
    import random
    for i in range(1000):
        l = []
        for j in range(random.randint(1,20)):
            l += [random.randint(1,100)]
        try:
            assert(median_of_median2(l)) == median_of_median(l)
        except:
            print(l)
            print('expect :',median_of_median(l))
            print('got :',median_of_median2(l))
            return 0
    print('--')
    
if __name__ == '__main__':
    #assert(median_of_median([59, 78, 29, 13, 22, 60, 12, 68, 77, 53, 3, 68, 43])) == 53
    test()
