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
    
    roman=""
    back=""
    
    roman = thousand*'M'.join([roman,back])
    if hundred < 5:
        if hundred == 4: roman = "CD".join([roman,back])
        else: roman = f"{hundred*'C'}".join([roman,back])
    else:
        if hundred < 9 and hundred >= 5: roman = f"D{(hundred-5)*'C'}".join([roman,back])
        else: roman = 'CM'.join([roman,back])
    if ten < 5:
        if ten == 4: roman = 'XL'.join([roman,back])
        else: roman = f"{ten*'X'}".join([roman,back])
    else:
        if ten < 9 and ten >= 5: roman = f"L{(ten-5)*'X'}".join([roman,back])
        else: roman = 'XC'.join([roman,back])
    if one < 5:
        if one == 4: roman = 'IV'.join([roman,back])
        else: roman = f"{one*'I'}".join([roman,back])
    else:
        if one < 9 and one >= 5: roman = f"V{(one-5)*'I'}".join([roman,back])
        else: roman = "IX".join([roman,back])
    return roman

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
    test()