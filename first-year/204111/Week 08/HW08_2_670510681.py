#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW08_2
# 204111 Sec 002

def skip_list(word:str) -> list[str]:
    n = len(word)

    # index
    def skip_str(n):
        if n <= 0:return [word]
        # list + next(list)
        now = [word[n::n+1]]
        next_ = skip_str(n-1)
        return now + next_

    return skip_str(n-1)[::-1]



if __name__ == "__main__":
    print(skip_list('AbCd'))
    print(skip_list('hello!'))
    print(skip_list('a'))
