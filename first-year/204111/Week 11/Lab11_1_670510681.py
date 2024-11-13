#!/usr/bin/env python3
# Atithep Thepkij(Tun)
# 670510681
# Lab11_1
# 204111 Sec 002
import string

def word_count(text:str) -> dict[str,int]:
    #txt = list(filter(lambda x: x.isalpha() or x.isspace() or x.isdigit(),text))
    #txt = "".join(txt).lower().split()
    txt = text.lower().split()
    punc = string.punctuation
    txt2 = []

    for i in txt:
        i = i.strip(punc)
        txt2.append(i)

    dict_,count = {},0
    for word in txt2:
        count = 1 + dict_.get(word,0)
        dict_[word] = count
    return dict_

if __name__ == "__main__":
    str_ = "\;He#$ doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care."
    print(word_count(str_))
    #assert word_count("He doesn't want to pay $40,000 for a new car, but his wife doesn't seem to care.") == {'new': 1,'but': 1,'pay': 1,'want': 1,'seem': 1,'care': 1,'his': 1,'40,000': 1,'wife': 1,'a': 1,'for': 1,'car': 1,"doesn't": 2,'to': 2,'he': 1}
    print("o ^ o")
