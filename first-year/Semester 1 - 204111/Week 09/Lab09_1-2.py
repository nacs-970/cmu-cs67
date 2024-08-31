#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab09_1
# 204111 Sec 002
def patterned_message(message: str, pattern:str,n=0) -> None:

    len_p = pattern.count('*')
    pattern = pattern.replace('*','{}')

    message = message.replace(' ','')
    len_m = len(message)

    # divmod
    #div_,remainder = divmod(len_p,len_m)
    #message = div_*message + message[:remainder]
    
    # compare
    if len_p > len_m: message = len_p*message # เพราะใน .format(*message) .format จะเอาที่ตรงกับ {} น้อยสุด คล้าย slicing เกิน

    print(pattern.format(*message))

if __name__ == '__main__':
    patterned_message("123", "*")
    patterned_message("123", "* ** * *** *** *")
