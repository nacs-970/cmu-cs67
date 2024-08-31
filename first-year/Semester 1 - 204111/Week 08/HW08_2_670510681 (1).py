#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW08_2
# 204111 Sec 002

def skip_list(word:str,step_=1) -> list[str]:
    len_ = len(word)
    if len_ == 1:return [word]
    now = [word[::step_]]
    next_ = skip_list(word[1:],step_+1)
    return now+next_

if __name__ == "__main__":
    print(skip_list('AbCd'))
    print(skip_list('hello!'))
    print(skip_list('a'))
