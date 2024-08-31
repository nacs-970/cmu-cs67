#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab06_2
# 204111 Sec 002

def dest_rotate_list(list_a: list[int],n:int) -> None:
    # + -> | - <-
    len_ = len(list_a)
    rotate = abs(n)%len_
    if n>0: list_a[:] = list_a[len_-rotate:] + list_a[:len_-rotate] # this also destructive with [:]
    else: list_a[:] = list_a[rotate:] + list_a[:rotate]
    return list_a

def test():
    list_a = [1,2,3,4]
    dest_rotate_list(list_a,1)
    assert list_a == [4,1,2,3]
    assert dest_rotate_list([1,2,3,4],1) == [4,1,2,3]
    assert dest_rotate_list([1,2,3,4],-1) == [2,3,4,1]
    assert dest_rotate_list([1,2,3,4],2) == [3,4,1,2]
    assert dest_rotate_list([1,2,3,4],-2) == [3,4,1,2]
    assert dest_rotate_list([1,2,3,4],3) == [2,3,4,1]
    assert dest_rotate_list([1,2,3,4],-3) == [4,1,2,3]
    assert dest_rotate_list([1,2,3,4],4) == [1,2,3,4]
    assert dest_rotate_list([1,2,3,4],-4) == [1,2,3,4]
    assert dest_rotate_list([1,2,3,4,5],3) == [3,4,5,1,2]
    assert dest_rotate_list([1,2,3,4,5],-3) == [4,5,1,2,3]
    assert dest_rotate_list([1,2,3,4],105) == [4,1,2,3]
    assert dest_rotate_list([1,2,3,4],-105) == [2,3,4,1]
    assert dest_rotate_list([1],-1) == [1]
    assert dest_rotate_list([1],1) == [1]
    print("> * <")

if __name__ == "__main__":
    #print(dest_rotate_list([1,2,3,4,5],-3))
    test()
