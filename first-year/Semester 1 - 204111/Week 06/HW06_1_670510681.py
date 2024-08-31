#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW06_1
# 204111 Sec 002

def uniform (line:str) -> str:
    #line2 = list(line) # turn into list

    # function
    #def check_lower(text): return text >= 'a'
    #def check_upper(text): return text >= 'A' and text < 'a'
    #low = len(list(filter(check_lower,line2))) # filter(function,array)
    #high = len(list(filter(check_upper,line2)))
    
    # ascii integer
    #low = len(list(filter(lambda x: x>= 'a',line2))) # filter(function,array) | count lower in array
    #high = len(list(filter(lambda x: x >= 'A' and x < 'a',line2))) 
    
    low = len(list(filter(lambda x: x.islower(),line)))
    high = len(list(filter(lambda x: x.isupper(),line)))
    alpha = list(filter(lambda x: x.isalpha(),line)) # list(filter(lambda x: x.isalpha(),line2))[0] get str of first index
    first = line.index(alpha[0]) # find first index of alphabet

    if low == high:
        if line[first].islower(): return line.lower()
        else: return line.upper()
    elif low > high: return line.lower()
    else: return line.upper()


def test():
    assert uniform("HaPpY") == "HAPPY"
    assert uniform("cOdINg") == "coding"
    assert uniform("coMp scI!!!") == "comp sci!!!"
    assert uniform("!coMp scI!!!") == "!comp sci!!!"
    print("# _ #")

if __name__ == "__main__":
    #print(uniform("HaPpy"))
    #print(uniform("AaaaAaa"))
    #print(uniform("cOdINg"))
    test()
