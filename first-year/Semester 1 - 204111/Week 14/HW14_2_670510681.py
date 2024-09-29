#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW14_2
# 204111 Sec 002
def bottom_up_m_sort(list_x: list[int], show_steps: bool=False) -> None:


    if show_steps:
        print(list(map(lambda x: x if isinstance(x,list) else [x],list_x)))

    if len(list_x) == 1:
        list_x[:] = list_x[0]
        return

    #print(list_x)

    len_ = len(list_x)//2
    rest = list_x[len_*2:]
    tmp = []

    # match
    for i in range(0,len_*2,2):
        #list_ = list_x[i:i+2]

        left = list_x[i:i+1]; right = list_x[i+1:i+2]

        if isinstance(left[0],list):
            left = left[0]
        if isinstance(right[0],list):
            right = right[0]

        len_l = len(left); len_r = len(right)
        i,j = 0,0
        bisec = []
        #print(left,right)
        while i < len_l and j < len_r:
            if left[i] < right[j]:
                bisec.append(left[i])
                i += 1
            else:
                bisec.append(right[j]) 
                j += 1
        if i < len_l:
            bisec.extend(left[i:])
        if j < len_r:
            bisec.extend(right[j:])
        #print(bisec)
        tmp.append(bisec)

    list_x[:] = tmp + rest
    bottom_up_m_sort(list_x,show_steps)
        #print(left,right)
    #print(tmp)

if __name__ == "__main__":
    list_x = [3, 7, 4, 9, 5, 2, 6] 
    bottom_up_m_sort(list_x, True) 
    print('--------') 
    print(list_x)
