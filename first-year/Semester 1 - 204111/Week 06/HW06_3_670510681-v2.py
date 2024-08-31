#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW06_3
# 204111 Sec 002

def moving_average(list_x:list[float],win_size:int) -> list[float]:
    if len(list_x) < win_size or win_size <= 0: return []
    if win_size == 1: return list_x

    #index_ = list(map(lambda x:list_x.index(x),list_x)) # [0,1,2,3,4]
    index_ = list(range(len(list_x)-(win_size-1))) # make an index and remove unwanted list
    avg = list(map(lambda x:(sum(list_x[x:x+win_size]))/win_size,index_)) # make list of sum with size of win_size
    return avg

def test():
    assert moving_average([1,2,3,4,5],2) == [1.5, 2.5, 3.5, 4.5] 
    assert moving_average([1,2,3,4,5],3) == [2.0, 3.0, 4.0] 
    assert moving_average([1,2,3,4,5],10) == []
    assert moving_average([1,2,3,4,5],-1) == []
    assert moving_average([1,2,3,4,5],1) == [1,2,3,4,5]
    print("! ^ !")

if __name__ == "__main__":
    test()
    print(moving_average([1,2,3],1))
