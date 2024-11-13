#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW09_2
# 204111 Sec 002
def median_of_median(list_a: list[float]) -> float:

    if len(list_a) == 3: 
        #min_ = min(list_a)
        #max_ = max(list_a)
        #mid_ = sum(list_a)-min_-max_
        return float(sum(list_a) - min(list_a) - max(list_a))

    if len(list_a) == 2:
        #return float(median(list_a))
        return float(sum(list_a)/2)

    if len(list_a) == 1:
        return float(list_a[0])

    step = len(list_a)//3
    step_a,step_b = step,2*step
    
    list_1 = list_a[:step_a]
    list_2 = list_a[step_a:step_b]
    list_3 = list_a[step_b:] # remainder will got median

    list_1 = median_of_median(list_1)
    list_2 = median_of_median(list_2)
    list_3 = median_of_median(list_3)

    return median_of_median([list_1,list_2,list_3]) # find median


if __name__ == '__main__':
    assert(median_of_median([59, 78, 29, 13, 22, 60, 12, 68, 77, 53, 3, 68, 43])) == 53
    print(median_of_median([1]))
