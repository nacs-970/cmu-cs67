#!/usr/bin/env python
# Atithep Thepkij (Tun)
# 670510681
# HW12_EX
# 204111 Sec 002


def xmas_tree(n:int):
    top = [" ",(" "*4) + (" "*n)+"|",(" "*3)+(" "*(n-1))+"--*--",(" "*4)+(" "*(n-1))+"/|\\"]; top2 = []

    for i in range(1,5):
        str_ = (" "*(4-i)) + (" "*(n-1)) + "/" + ("* "*(i)) + "*" + "\\"
        top.append(str_)

    truck = [((" "*4) + (" "*(n-1)) + "|||" + (" "*4) + (" "*(n-1))),(("_"*4) + ("_"*(n-1)) + "|||" + ("_"*4) + ("_"*(n-1)))]

    ans = top + truck

    if n == 1:
        ans = "\n".join(ans)
        return ans

    body = []

    for i in range(n-1):
        for j in range(1,4):
            str_ = (" "*(n-i-j+1)+"/"+("* "*(j+i+2))+ ("*")+"\\")
            body.append(str_)
    
    ans = top + body + truck
    ans = "\n".join(ans)
    return ans


if __name__ == "__main__":
    xmas_tree(1)
    #xmas_tree(2)
    xmas_tree(3)
    xmas_tree(4)
