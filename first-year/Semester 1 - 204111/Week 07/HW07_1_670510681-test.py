#!/usr/bin/env python3
# Atithep Thepkij
# 670510681
# HW07_1
# 204111 Sec 002

DEBUG = False

def print_polynomial(pc_list: list[tuple[int,float]], var: str) -> str:
    # tuple[power,coefficient]
    
    pc_list = sorted(pc_list,key = lambda x: x[1],reverse=True) # sort coefficient
    pc_list = sorted(pc_list,key = lambda x: x[0],reverse=True) # sort power
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
        if power[index_] in power_filter: poly += '^' + str(power[index_]) # ^Power

        return poly

    poly = list(map(function_,range_))
    poly = ''.join(poly)
    if poly == '': return 0
    return poly

def check_list(v,l_a,l_b):
   if l_b == 0:
       if l_a == 0:
           return ''
       elif l_a > 0:
           return '+ '+str(l_a)
       elif l_a <= 0:
           return '- '+str(abs(l_a))
   elif l_b == 1:
       if l_a == 1:
           return '+ '+v
       elif l_a == -1:
           return '- '+v
       elif l_a == 0:
           return ''
       elif l_a > 0:
           return '+ '+str(l_a)+v
       elif l_a < 0:
           return '- '+str(abs(l_a))+v
   elif l_b > 1:
       if l_a == 1:
           return '+ '+v+'^'+str(l_b)
       elif l_a == -1:
           return '-'+v+'^'+str(l_b)
       elif l_a == 0:
           return ''
       elif l_a > 0:
           return '+ '+str(l_a)+v+'^'+str(l_b)
       elif l_a < 0:
           return '- '+str(abs(l_a))+v+'^'+str(l_b)

def print_polynomial2(pc_list: list[tuple[int,float]], v: str) -> str:

    if pc_list == []:
        return '0'

    pc_list = list(reversed(sorted(pc_list)))
    range_pc = list(range(0,len(pc_list)))
    b = list(map(lambda x: list(pc_list[x])[0],range_pc))
    a = list(map(lambda x: list(pc_list[x])[1],range_pc))

    result = list(map(lambda x,y: str(check_list(v,x,y)),a,b))
    result = list(filter(lambda x: x != '' ,result))
    result = ' '.join(result)

    if result == '':
        return '0'
    elif result[0] == '+':
        return result[2:]
    elif result[0:2] == '- ':
        return '-'+result[2:]
    else:
        return result

def random_():
    import random
    import string
    for i in range(1000):
        n = random.randint(0,10)
        l = list(map(lambda x: (random.randint(0,20),random.randint(-10,10)),range(n)))
        var = random.choice(string.ascii_letters)
        try:
            assert print_polynomial2(l,var) == print_polynomial(l,var)
        except:
            print(l,var)
            print('Exp :',print_polynomial(l,var))
            print('Got :',print_polynomial2(l,var))
            return 0

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
    assert print_polynomial([(1,-1)],"y") == '-y'
    print(";P o P;")

if __name__ == "__main__":
    random_()
    #test()

