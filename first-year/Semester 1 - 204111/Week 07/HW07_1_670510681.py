#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# HW07_1
# 204111 Sec 002

def print_polynomial(pc_list: list[tuple[int,float]], var: str) -> str:
    # tuple[power,coefficient]

    pc_list = sorted(pc_list,key = lambda x: x[0],reverse=True)
    pc_list = list(filter(lambda x: x[1] != 0,pc_list)) # remove zero coefficient
    range_ = list(range(len(pc_list)))

    power = list(map(lambda x: x[0],pc_list)) # similar to zip
    coefficient = list(map(lambda x: x[1],pc_list))

    abs_coefficient = list(map(lambda x: abs(x[1]),pc_list))

    positive = list(filter(lambda x: x>=0,coefficient))
    power_filter = list(filter(lambda x: x>1,power))
    
    # -/+ number ^ power
    def function_(index_):
        
        poly = ""
        # Plus , Minus
        if index_ > 0 and coefficient[index_] in positive: poly += " + "
        elif index_ == 0 and coefficient[index_] not in positive: poly += "-" # Front
        elif index_ == 0 and coefficient[index_] in positive: poly += "" # Front
        else: poly += " - "

        # Number
        if abs_coefficient[index_] == 1 and power[index_] == 0: return poly + '1'
        if abs_coefficient[index_] != 1: poly += str(abs_coefficient[index_])

        # Power
        if power[index_] >= 1: poly += var
        if power[index_] in power_filter: poly += '^'
        if power[index_] in power_filter: poly += str(power[index_])

        return poly

    poly = list(map(function_,range_))
    poly = ''.join(poly)
    if poly == '': return 0
    return poly
    
 #   poly = list(map(lambda x: f'{" + " if x > 0 and coefficient[x] in positive else "-" if coefficient[x] == coefficient[0] and coefficient[x] not in positive else "" if coefficient[x] == coefficient[0] else " - "}{abs_coefficient[x]}'\
 #       + f'{v*(1 if power[x] >= 1 else 0)}'\
 #       + f'{"^"*(1 if power[x] in power_filter else 0)}{power[x] if power[x] in power_filter else ""}',range_))

def test():
    assert print_polynomial([(2, -6), (0, -8), (1, 34)],'x') == '-6x^2 + 34x - 8'
    assert print_polynomial([(4, -6), (2, -8), (3, 34)],'x') == '-6x^4 + 34x^3 - 8x^2'
    assert print_polynomial([(2, -6), (0, -8), (1, 34)],'y') == '-6y^2 + 34y - 8'
    assert print_polynomial([(2, 6), (0, -8), (1, 34)],'y') == '6y^2 + 34y - 8'
    assert print_polynomial([(2, 6.5), (0, -8)],'y') == '6.5y^2 - 8'
    assert print_polynomial([(4, -6), (2, -8), (3, 34),(6,34),(1,5)],'x') == '34x^6 - 6x^4 + 34x^3 - 8x^2 + 5x'
    assert print_polynomial([(4, -6), (2, -8), (3, 0)],'x') == '-6x^4 - 8x^2'
    assert print_polynomial([(0, 0), (1, 0)],'y') == 0
    assert print_polynomial([(0, 0), (1, 1)],'y') == 'y'
    assert print_polynomial([(1, 0), (0, 1)],'y') == '1'
    assert print_polynomial([(1, 0), (0, -1)],'y') == '-1'
    assert print_polynomial([(1, 0), (0, -2)],'y') == '-2'
    assert print_polynomial([(1, 1), (0, -2)],'y') == 'y - 2'
    assert print_polynomial([(1, 1), (0, 1)],'y') == 'y + 1'
    assert print_polynomial([(1,-1)],"y") == '-y'
    assert print_polynomial([(0,4)],"y") == '4'
    assert print_polynomial([(0,1)],"y") == '1'
    print(";P o P;")

if __name__ == "__main__":
    test()
