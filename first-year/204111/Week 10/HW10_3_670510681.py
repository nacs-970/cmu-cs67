#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# HW10_2
# 204111 Sec 002
def polynomial_addition(p1: list[tuple[int, float]], p2: list[tuple[int, float]]) -> list[tuple[int, float]]:
    # x[0] power x[1] coefficient
    p1 = sorted(p1,key=lambda x: x[1],reverse=True)
    p1 = sorted(p1,key=lambda x: x[0],reverse=True)

    p2 = sorted(p2,key=lambda x: x[1],reverse=True)
    p2 = sorted(p2,key=lambda x: x[0],reverse=True)

    len_p1,len_p2 = len(p1),len(p2)
    i,j = 0,0
    list_ = []

    while i < len_p1 and j < len_p2:

        p1power = p1[i][0]
        p2power = p2[j][0]

        p1coeff = p1[i][1]
        p2coeff = p2[j][1]

        if p1power == p2power:
            res = p1coeff + p2coeff
            if res != 0:
                list_.append((p1power,res))
            i += 1
            j += 1
        if p1power > p2power:
            list_.append(p1[i])
            i += 1
        if p1power < p2power:
            list_.append(p2[j])
            j += 1

    if i < len_p1:
        list_.extend(p1[i:]) 
    if j < len_p2:
        list_.extend(p2[j:]) 

    return list_
if __name__ == "__main__":

    p1 = [(2, 6), (1, 34), (0, -8),(3,10)] 
    p2 = [(2, -6), (0, 2), (1, 1)] 

    print(polynomial_addition(p1,p2))

