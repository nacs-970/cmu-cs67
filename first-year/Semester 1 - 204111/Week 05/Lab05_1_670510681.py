#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab05_01
# 204111 Sec 002

def main():
    test()

def palindrome_without(text:str,c:str) -> bool:
    text = text.lower()
    c = c.lower()
    text = text.replace(c,"")
    text = text.replace(" ","") # "a a a" != "aaa" in python
    if text =="": return False
    elif text == text[::-1]: return True
    else: return False

def test():
    assert palindrome_without("Banana","b") == True
    assert palindrome_without("T","t") == False
    assert palindrome_without("Swap of paws","f") == True
    assert palindrome_without("a a a"," ") == True
    print(":)")
if __name__ == "__main__":
    main()
