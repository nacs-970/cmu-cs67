#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW03_3
# 204111 Sec 002

num = int(input())
k = int(input())
val = int(input())

# Get index postion
def set_kth_digit(num,k,val):

    # find index value
    num2 = num//10**k%10

    # ex: 1,2,5
    # num2 = 0
    # val = (5 - 0)*10^2
    # num += val (1+500)
    # ex: 2343,2,7
    # num2 = 3
    # val = (7 - 3)*10^2
    # num += val (2343+400)

    val = (val - num2)*10**k
    num += val
    return num

print(set_kth_digit(num,k,val))
