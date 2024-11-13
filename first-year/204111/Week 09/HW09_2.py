#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW09_2
# 204111 Sec 002
def median_of_median(list_a: list[float]) -> float:
    
    if len(list_a) == 0:return 0

    def median(list_):
        len_ = len(list_)
        mid = len_//2
        if len_%2 == 1: return list_[mid]
        return (list_[mid] + list_[mid-1])/2

    def sort_(list_):
        if len(list_) == 1: return list_
        min_ = min(list_)
        list_.remove(min_)
        return [min_] + sort_(list_)

    if len(list_a) <= 3: return float(median(list_a))

    if len(list_a) > 3:
        step = len(list_a)//3
        remainder = len(list_a)%3

        if step*3 == len(list_a): step_a,step_b,step_c = step,step,step
        step_a,step_b,step_c = step,step,step+remainder

        list_1 = list_a[:step_a]
        list_2 = list_a[step_a:step_a+step_b]

        if remainder > 0:
            list_3 = list_a[step_a+step_b:-remainder]
            list_3[-1] = [list_3[-1]] + list_a[-remainder:]
            list_3[-1] = sum(list_3[-1])/len(list_3[-1])
        else:
            list_3 = list_a[step_a+step_b:]

    #def sort_(list_,index_):
    #    if index_ == 0:return list_
    #    now = list_[index_]
    #    next = sort_(list_,index_-1)
    #    if now < list_[index_-1]:
    #        list_[index_-1],list_[index_] = list_[index_],list_[index_-1]
    #    return sort_(list_,index_-1)

    #list_1 = sort_(list_1,len(list_1)-1)
    #list_2 = sort_(list_2,len(list_2)-1)
    #list_3 = sort_(list_3,len(list_3)-1)
    #print(list_1,list_2,list_3)

    list_1 = sort_(list_1)
    list_2 = sort_(list_2)
    list_3 = sort_(list_3)

    mandm = [median(list_1)] + [median(list_2)] + [median(list_3)]
    return float(median(mandm))


if __name__ == '__main__':
    print(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]))
    print(median_of_median([1,2,3,4,5,6,7]))
    print(median_of_median([1,2,3,4,5]))
    print(median_of_median([1,2,3,4,5,6]))
    print(median_of_median([1]))
    print(median_of_median([]))
