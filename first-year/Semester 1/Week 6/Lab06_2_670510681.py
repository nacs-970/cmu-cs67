#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab06_2
# 204111 Sec 002

def dest_rotate_list(list_a: list[int],n:int) -> None:
    # + -> | - <-
    len_ = len(list_a)
    rotate = abs(n)%len_
    if n>0:
        # len = 5 , n = 3 ,[1,2,3,4,5]
        #print(list_a[len_-rotate:])  # [2:] [3,4,5]
        #print(list_a[:len_-rotate])  # [:2] [1,2]

        list_a.extend(list_a[len_-rotate:]) # [1,2,3,4,5,3,4,5]
        list_a.extend(list_a[:len_-rotate]) # [1,2,3,4,5,3,4,5,1,2]
        del list_a[:len_] # remove front 0 to len_

        #list_a.insert(0,list_a[-1])
        #del list_a[-1]
        #list_a = [list_a[-1]] + [list_a[0]] + list_a[1:-1]

        #return list_a
    else:
        # len = 5 , n = -3 ,[1,2,3,4,5]
        #print(list_a[rotate:]) #[3:]
        #print(list_a[:rotate]) #[:3]

        list_a.extend(list_a[rotate:]) # [1,2,3,4,5,4,5]
        list_a.extend(list_a[:rotate]) # [1,2,3,4,5,4,5,3,2,1]
        del list_a[:len_] # remove front 0 to len_

        #list_a.append(list_a[0])
        #del list_a[0]
        #list_a = list_a[1:-1] + [list_a[0]] + [list_a[-1]]

        #return list_a

def test():
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
