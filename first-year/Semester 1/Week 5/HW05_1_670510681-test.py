#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW05_1
# 204111 Sec 002
import random
import string

def substitute_once(text:str,old:str,new:str) -> str:
    search = text.find(old) # find first match str
    if old == "" or search == -1: return text
    # replace old with new and display the rest of text start behide old
    #return text[:search]+new+text[search+len(old):] 
    f = text[:search]
    b = text[search+len(old):]
    return new.join([f,b])

def substitute_once_2(text: str, old: str, new: str) -> str:
    
    if " " == text and "" == old:
        return text
    elif old in text:   
        if text.startswith(old):
            position_old = len(old)
            newstr = "".join([new,text[position_old:]])
            return newstr
            
        elif text.endswith(old):
            position_old = len(text) - len(old)
            newstr = "".join([text[:position_old],new])
            return newstr
        
        else:
            if len(text)-(len(text)-len(old))== 1:
                position_front = len(text)-(len(text)-len(old))
                position_back = len(old) - len(text)+1
            elif len(old)>=3:
                position_front = text.find(old,0,)
                position_back = len(old) - len(text)+2
            else:
                position_front = len(text)-(len(text)-len(old))-1
                position_back = len(old) - len(text)+1

            newstr = text[:position_front] + new + text[position_back:]
            return newstr
    else:
        return text

def test():
    for i in range(100000):
        letter = "qwertyuiop[]\\asdfghjkl;\'zxcvbm,./1234567890-=`~QWERTYUIOPASDFGHJKLZXCVBNM %|<>{}°@#$_&-+()*\":;!?/•√π÷×§∆…£¢€¥^°©®™✓¿"
        text = ""
        a=""
        b=""
        for i in range(random.randint(1,10)):
            text += random.choice(letter)
        for i in range(random.randint(1,10)):
            a += random.choice(letter)
        for i in range(random.randint(1,10)):
            b += random.choice(letter)
        try:
            assert substitute_once_2(text,a,b) == substitute_once(text,a,b)
        except:
            raise b
            print(" | ",text," | ",a," | ",b," | ")
            print(f"expect:  {substitute_once(text,a,b)}  got:  {substitute_once_2(text,a,b)}")
            return 0
    #print("o u o")
    #assert substitute_once("battle","b","c") == "cattle"
    #assert substitute_once("Bidding","i","u") == "Budding"
    #assert substitute_once("doesn't","n't"," not") == "does not"
    #assert substitute_once("ab","b","bbb") == "abbb"
    #assert substitute_once("  ","","=") == "  "
    #assert substitute_once('baaaaaab','aaa','c') == 'bcaaab'
    print("\" ° ^ ° \"")

if __name__ == "__main__":
    test()