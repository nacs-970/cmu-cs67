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

    #def sort_(list_):
    #    if len(list_) == 1: return list_
    #    min_ = min(list_)
    #    list_.remove(min_)
    #    return [min_] + sort_(list_)

    if len(list_a) == 3: 
        min_ = min(list_a)
        max_ = max(list_a)
        mid_ = sum(list_a)-min_-max_
        return float(median([min_,mid_,max_]))

    if len(list_a) <= 2:
        #return float(sum(list_a)/2)
        return float(median(list_a))
    #if len(list_a) == 1:
    #    return float(list_a[0])

    step = len(list_a)//3
    step_a,step_b = step,2*step
    
    list_1 = list_a[:step_a]
    list_2 = list_a[step_a:step_b]
    list_3 = list_a[step_b:] # remainder will got median

    list_1 = median_of_median(list_1)
    list_2 = median_of_median(list_2)
    list_3 = median_of_median(list_3)

    return median_of_median([list_1,list_2,list_3]) # find median
    #return [median_of_median(list_1),median_of_median(list_2),median_of_median(list_3)]
    #return median([median_of_median(list_1),median_of_median(list_2),median_of_median(list_3)])

    #if remainder > 0:
    #    list_3[-1] = [list_3[-1]] + list_a[-remainder:]
    #    list_3[-1] = sum(list_3[-1])/len(list_3[-1])

    #print(list_1,list_2,list_3)

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
    
    #list_1 = sort_(list_1)
    #list_2 = sort_(list_2)
    #list_3 = sort_(list_3)

    #mandm = [median(list_1)] + [median(list_2)] + [median(list_3)]
    #return float(median(mandm))
    
    #a = sum(list_1) - min(list_1) - max(list_1)
    #b = sum(list_2) - min(list_2) - max(list_2)
    #c = sum(list_3) - min(list_3) - max(list_3)

    #return float(median([a,b,c]))


if __name__ == '__main__':
    #print(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16,54,53,45,345,3,7,654,1,23,5,368,85,2346,246,8,34,562,3,45,2345, 3,56,65,4,546,4,64,65,464,56,423,4,23434,765]))
    #print(median_of_median([28,29,87, 14, 13, 21, 19, 27, 23, 30, 16, 3]))
    #print(median_of_median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]))
    #print(median_of_median([1,1,1,1,1,1,1,1,1]))
    #print(median_of_median([1,2,3,4,5,6,7,8,9]))
    #print(median_of_median([1,1,1,1,1,1,1,1]))
    #print(median_of_median([1,2,3,4,5,6,7,8]))
    #print(median_of_median([1,2,3,4,5,6,7]))
    #print(median_of_median([1,2,3,4,5,6]))
    #print(median_of_median([1,2,3,4,5]))
    #print(median_of_median([1,2,3,4]))
    #print(median_of_median([4,2,3.2,2.7,1]))
    #print(median_of_median([1,3,2.5]))
    #print(median_of_median([5,6,2]))
    #print(median_of_median([1,2]))

    #[59, 78, 29, 13] [22, 60, 12, 68] [77, 53, 3, 68, 43]
    #[59] [78] [29, 13] -> 59
    #[22] [60] [12, 68] -> 40
    #[77] [53] [3, 68, 43] -> 53
    # 53

    print(median_of_median([59, 78, 29, 13, 22, 60, 12, 68, 77, 53, 3, 68, 43])) # 53
    #print(median_of_median([1]))
