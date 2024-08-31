#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW05_3
# 204111 Sec 002

def is_valid_license(license_str:str) -> bool:
    # NCCNNNN | CCNNNN | CNCNNNN
    if len(license_str) > 7: return False
    
    # first 3
    if (license_str[0].isdigit() and license_str[1:3].isalpha()):
        if license_str[3:].isdigit():
            #print(license_str[3:])
            return True
        #print(license_str[0:3])
        return False
        
    # first 2
    elif license_str[0:2].isalpha():
        if license_str[2:].isdigit() and len(license_str[2:])<=4:
            #print(license_str[2:])
            return True
        #print(license_str[0:2])
        return False
    
    else:
        #print(license_str[:3])
        return False

def test():
    assert is_valid_license("CD700") == True
    assert is_valid_license("9AB8954") == True
    assert is_valid_license("9999") == False
    assert is_valid_license("99D1234") == False
    assert is_valid_license("9AB89A4") == False
    assert is_valid_license("9C4567") == False
    assert is_valid_license("AB444A") == False
    assert is_valid_license("AA11111") == False
    print("$ u $")
    
if __name__ == "__main__":
    test()
    #print(is_valid_license("CD09999"))