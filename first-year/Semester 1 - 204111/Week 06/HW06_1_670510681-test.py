#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW06_1
# 204111 Sec 002
import string
import random
def uniform (line:str) -> str:
    line2 = list(line) # turn into list

    low = len(list(filter(lambda x: x.islower(),line2)))
    high = len(list(filter(lambda x: x.isupper(),line2)))
    alpha = list(filter(lambda x: x.isalpha(),line2)) # list(filter(lambda x: x.isalpha(),line2))[0] get str of first index
    first = line.index(alpha[0]) # find first index of alphabet

    if low == high:
        if line[first].islower():
            return line.lower()
        else:
            return line.upper()
    elif low > high:
        return line.lower()
    else:
        return line.upper()

def uniform_2(line:str)->str:
    upper = filter(lambda x: x in string.ascii_uppercase,line)
    num_upper = len(list(upper))
    num_lower = len(list(line)) - num_upper
    if num_upper == num_lower:
        if line[0] in string.ascii_uppercase:
            line = ''.join(line)
            return (line.upper())
        elif line[0] in string.ascii_lowercase:
            line = ''.join(line)
            return (line.lower())
        else:
            return None
    elif num_upper > num_lower:
        line = ''.join(line)
        return (line.upper())
    else:
        line = ''.join(line)
        return (line.lower())

def test():
    assert uniform("HaPpY") == "HAPPY"
    assert uniform("cOdINg") == "coding"
    assert uniform("coMp scI!!!") == "comp sci!!!"
    assert uniform("!coMp scI!!!") == "!comp sci!!!"
    for i in range(100000):
        letter = ""
        for j in range(random.randint(1,5)):
            letter += random.choice(string.ascii_letters+string.digits)
        try:
            assert uniform_2(letter) == uniform(letter)
        except:
            print(letter)
            print("expect :", uniform(letter), "got :", uniform_2(letter))
            return 0
    print("# _ #")

if __name__ == "__main__":
    #print(uniform("HaPpy"))
    #print(uniform("AaaaAaa"))
    #print(uniform("cOdINg"))
    test()
