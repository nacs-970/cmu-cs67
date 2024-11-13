#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW03_3
# 204111 Sec 002

def main():
    num,k,val = int(input()),int(input()),int(input())
    print(set_kth_digit(num,k,val))

def kth_digit(num:int,k:int) -> int:
    num = abs(num)
    num = num//10**k%10
    return num

# Get index postion
def set_kth_digit(num:int,k:int,val:int) -> int:

    # find index value
    num2 = kth_digit(num,k)

    # ex: 1,2,5
    # num2 = 0
    # val = (5 - 0)*10^2
    # num += val (1+500)

    # ex: 2343,2,7
    # num2 = 3
    # val = (7 - 3)*10^2
    # num += val (2343+400)

    # ex: 2343,2,1
    # num2 = 3
    # val = (1 - 3)*10^2
    # num += val (2343-200)

    val = (val - num2)*10**k
    num += val
    return num

if __name__ == "__main__":
    main()
