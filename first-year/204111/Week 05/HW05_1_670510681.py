#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW05_1
# 204111 Sec 002

def substitute_once(text:str,old:str,new:str) -> str:
    search = text.find(old) # find first match str
    if old == "" or search == -1: return text
    # replace old with new and display the rest of text start behide old
    #return text[:search]+new+text[search+len(old):] 
    f = text[:search]
    b = text[search+len(old):]
    return new.join([f,b])

def test():
    assert substitute_once("battle","b","c") == "cattle"
    assert substitute_once("Bidding","i","u") == "Budding"
    assert substitute_once("doesn't","n't"," not") == "does not"
    assert substitute_once("ab","b","bbb") == "abbb"
    assert substitute_once("  ","","=") == "  "
    assert substitute_once('baaaaaab','aaa','c') == 'bcaaab'
    print("\" ° ^ ° \"")

if __name__ == "__main__":
    test()