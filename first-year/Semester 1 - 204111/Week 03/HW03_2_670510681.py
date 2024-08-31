#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW03_2
# 204111 Sec 002

#abs() = abosulute number
def main():
    num,k = int(input()),int(input())
    print(kth_digit(num,k))

def kth_digit(num:int,k:int) -> int:

    # number floor division with 10^k 
    # mod % 10
    # ex : 
    # 789 // 10^1 = 78
    # 78 % 10 = 8
    # ex : 
    # 789 // 10^0 = 789
    # 789 % 10 = 9
    num = abs(num)
    num = num//10**k%10
    return num

if __name__ == "__main__":
    main()
