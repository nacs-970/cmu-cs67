#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW03_2
# 204111 Sec 002
num = int(input())
k = int(input())
def kth_digit(num,k):

    # number floor division with 10^k 
    # mod % 10
    # ex : 
    # 789 // 10^1 = 78
    # 78 % 10 = 8
    # ex : 
    # 789 // 10^0 = 789
    # 789 % 10 = 9

    num = num//10**k%10
    return num

print(kth_digit(num,k))
