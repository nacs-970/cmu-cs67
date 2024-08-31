#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW05_2
# 204111 Sec 002
from random import randint

def roman_numeral(n: int) -> str:

    hundred = n%1000
    thousand = n // 1000
    ten = hundred%100
    hundred = hundred//100
    one = ten%10
    ten = ten//10
    #print(thousand,hundred,ten,one)
    roman=""
    back=""
    
    romantable = "IVXLCDM" # 1 5 10 50 100 500 1000
    #return thousand,hundred,ten,one
    #return f"V{(one-5)*'I'}"
    #roman += thousand*'M'
    roman = thousand*'M'.join([roman,back])
    if hundred < 5:
        if hundred == 4:
            #roman += "CD"
            roman = "CD".join([roman,back])
        else:
            #roman += hundred*'C'
            roman = f"{hundred*'C'}".join([roman,back])
    else:
        if hundred < 9 and hundred >= 5:
            #roman += f"D{+(hundred-5)*'C'}"
            roman = f"D{(hundred-5)*'C'}".join([roman,back])
        else:
            #roman += 'CM'
            roman = 'CM'.join([roman,back])
    if ten < 5:
        if ten == 4:
            #roman += "XL"
            roman = 'XL'.join([roman,back])
        else:
            #roman += ten*'X'
            roman = f"{ten*'X'}".join([roman,back])
    else:
        if ten < 9 and ten >= 5:
            #roman += "L"+(ten-5)*'X'
            roman = f"L{(ten-5)*'X'}".join([roman,back])
        else:
            #roman += 'XC'
            roman = 'XC'.join([roman,back])
    if one < 5:
        if one == 4:
            #roman += "IV"
            roman = 'IV'.join([roman,back])
        else:
            #roman += one*'I'
            roman = f"{one*'I'}".join([roman,back])
    else:
        if one < 9 and one >= 5:
            #roman += "V"+(one-5)*'I'
            roman = f"V{(one-5)*'I'}".join([roman,back])
        else:
            #roman += 'IX'
            roman = "IX".join([roman,back])
    return roman

def roman_numeral_check(n: int) -> str:

    hundred = n%1000
    thousand = n // 1000
    ten = hundred%100
    hundred = hundred//100
    one = ten%10
    ten = ten//10
    #print(thousand,hundred,ten,one)
    roman=""

    romantable = "IVXLCDM" # 1 5 10 50 100 500 1000
    #return thousand,hundred,ten,one
    
    roman += thousand*'M'
    if hundred <= 5:
        if hundred == 5:
            roman += 'D'
        elif hundred == 4:
            roman += "CD"
        else:
            roman += hundred*'C'
    else:
        if hundred < 9 and hundred >= 6:
            roman += f"D{(hundred-5)*'C'}"
        else:
            roman += 'CM'
    if ten <= 5:
        if ten == 5:
            roman += 'L'
        elif ten == 4:
            roman += "XL"
        else:
            roman += ten*'X'
    else:
        if ten < 9 and ten >= 6:
            roman += f"L{(ten-5)*'X'}"
        else:
            roman += 'XC'
    if one <= 5:
        if one == 5:
            roman += 'V'
        elif one == 4:
            roman += "IV"
        else:
            roman += one*'I'
    else:
        if one < 9 and one >= 6:
            roman += f"V{(one-5)*'I'}"
        else:
            roman += 'IX'
    return roman

def test():
    n = randint(1,4999)
    for i in range(9999):
        try:
            assert roman_numeral(n) == roman_numeral_check(n)
        except:
            print(n)
            print(f"expect :{roman_numeral_check(n)} | got : {roman_numeral(n)}")
            return 0
    print(":)")

if __name__ == "__main__":
    test()