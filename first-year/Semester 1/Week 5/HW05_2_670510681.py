#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW05_2
# 204111 Sec 002

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
    
    romantable = "I,V,X,L,C,D,M" # 1 5 10 50 100 500 1000
    #return thousand,hundred,ten,one
    #return f"V{(one-5)*'I'}"
    #roman += thousand*'M'
    roman = thousand*'M'.join([roman,back])
    # hundred
    if hundred < 5:
        if hundred == 4:
            #roman += "CD"
            roman = "CD".join([roman,back])
        else:
            #roman += hundred*'C'
            roman = f"{hundred*'C'}".join([roman,back]) # if no f-string mean hundred * ('C'.join([roman,back]))
    else:
        if hundred < 9 and hundred >= 5:
            #roman += f"D{+(hundred-5)*'C'}"
            roman = f"D{(hundred-5)*'C'}".join([roman,back])
        else:
            #roman += 'CM'
            roman = 'CM'.join([roman,back])
    # ten
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
    # one
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
    #M = n
    #roman += (M//1000)*'M'
    #D = M%1000
    #roman += (D//500)*'D'
    #C = D%500
    #roman += (C//100)*'C'
    #L = C%100
    #roman += (L//50)*'L'
    #X = L%50
    #roman += (X//10)*'X'
    #V = X%10
    #roman += (V//5)*'V'
    #I = V%5
    #roman += (I//1)*'I'

def test():
    assert roman_numeral(4) == "IV"
    assert roman_numeral(9) == "IX"
    assert roman_numeral(25) == "XXV"
    assert roman_numeral(47) == "XLVII"
    assert roman_numeral(67) == "LXVII"
    assert roman_numeral(3575) == "MMMDLXXV"
    assert roman_numeral(4999) == "MMMMCMXCIX"
    print(":)")

if __name__ == "__main__":
    #print(roman_numeral(4))
    #print(roman_numeral(9))
    #print(roman_numeral(25))
    #print(roman_numeral(47))
    #print(roman_numeral(57))
    #print(roman_numeral(3575))
    #print(roman_numeral(4999))
    #print(roman_numeral(2122))
    test()