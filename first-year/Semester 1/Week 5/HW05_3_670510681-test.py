#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW05_3
# 204111 Sec 002

import random

def is_valid_license(license_str:str) -> bool:
    if len(license_str) > 7: return False
    
    if (license_str[0].isdigit() and license_str[1:3].isalpha()):
        if license_str[3:].isdigit(): return True
        return False
        
    elif license_str[0:2].isalpha():
        if license_str[2:].isdigit() and len(license_str[2:])<=4: return True
        return False
    
    else: return False

def is_valid_license_2(license_str:str) -> bool:
    if len(license_str) > 7: return False

    if (license_str[0].isdigit() and license_str[1:3].isalpha()):
        if license_str[3:].isdigit():return True
        return False
    elif license_str[0:2].isalpha():
        if license_str[2:].isdigit() and len(license_str[2:])<=4:return True
        return False
    
    else: return False
def test():
    #assert is_valid_license("CD700") == True
    #assert is_valid_license("9AB8954") == True
    #assert is_valid_license("9999") == False
    #assert is_valid_license("99D1234") == False
    #assert is_valid_license("9AB89A4") == False
    #assert is_valid_license("9C4567") == False
    #assert is_valid_license("AB444A") == False
    #assert is_valid_license("AA11111") == False
    letter = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"
    for i in range(10000):
        license_ = ""
        for i in range(random.randint(1,10)):
            license_ += random.choice(letter)
        try:
            assert is_valid_license_2(license_) == is_valid_license(license_)
        except:
            print(license_)
            print("expect",is_valid_license(license_),"got",is_valid_license_2(license_))
            return 0
    print("$ u $")
    
if __name__ == "__main__":
    test()
