#!/usr/bin/env python
# 670510681
# Atithep Thepkij (Tun)
# HW13_1
# 204111 Sec 002

def product_shopping(p_list: dict[str, tuple[float, float]],allowed_w: float, budget: float) -> dict[str, float]:
    # 0 < budget <= 10000
    # 5 <= allowed_w <= 1000

    # power set
    set_ = [[]]
    list_ = list(p_list.keys())
    for i in list_:
        q = map(lambda x: x + [i],set_.copy())
        set_ += q
    filter_ = []

    # filter exceed allowed_w and budget
    for list_ in set_:
        wc,bc = 0,0
        for n in list_:
            wc += p_list.get(n)[0]
            bc += p_list.get(n)[1]

        if wc <= allowed_w and bc <= budget:
            filter_.append(list_)

    filter_ = filter_[1:][::-1]
    #print(filter_)
    
    # find the best pattern
    ans = []
    max_len,min_weight,min_budget = 0,allowed_w,budget
    #print(allowed_w,budget)
    for list_ in filter_:
        wc,bc = 0,0
        for n in list_:
            wc += p_list.get(n,(0,0))[0]
            bc += p_list.get(n,(0,0))[1]
        #print(list_,wc,bc)

        if len(list_) >= max_len:
            max_len = len(list_)
            #print("hit")
            #print(list_,wc,bc)
            if wc == min_weight and bc < min_budget:
                min_budget = bc
                ans = list_

            if wc < min_weight:
                min_weight = wc
                min_budget = bc
                ans = list_

        ans = sorted(ans)
                #if bc < min_budget:
                #print(list_,wc,bc)
                    #print(ans)
    d = dict(map(lambda x: (x,p_list.get(x)[0]),ans))
    #print(d)
    return d

import random
import string
def test():
    for i in range(1000):
        d = {}

        for i in range(random.randint(1,15)):
            char = random.choice(string.ascii_lowercase)
            d[char] = (float(f"{random.uniform(0,100):.2f}"),float(f"{random.uniform(5,100):.2f}"))

        w,b = float(f"{random.uniform(0,100):.2f}"),float(f"{random.uniform(5,100):.2f}")

        if product_shopping(d,w,b) == {} or len(product_shopping(d,w,b)) <= 3:
            continue
        print("---")
        print("p_list =", d)
        print("allowed_w =",w)
        print("budget =",b)
        print("ans :",product_shopping(d,w,b))


if __name__ == "__main__":
    assert product_shopping({"table": (5, 900.), "chair": (0.4, 450.),"pillow": (3.5, 1200), "stool": (0.3, 300.0)},25.0,2500.00) == {'stool': 0.3,'chair': 0.4,'pillow': 3.5}
    assert product_shopping({"chair": (0.4, 450.0), "pillow": (3.5, 315.0),"stool": (0.3, 300.0), "closet": (2.5, 700.0)}, 15.0,1450.00) == {'stool': 0.3,'chair': 0.4,'closet': 2.5}
    product_shopping({"a":(0.1,10)},100.0,100.0)
    product_shopping({"a":(0.1,10)},100.0,1.0)
    test()
    #p_list = {"table": (5, 900.), "chair": (0.4, 450.),"pillow": (3.5, 1200), "stool": (0.3, 300.)}
    #allowed_w = 25.0
    #budget = 2500.00
    #product_shopping(p_list, allowed_w, budget)
    #p_list = {"chair": (0.4, 450.0), "pillow": (3.5, 315.0),
    #"stool": (0.3, 300.0), "closet": (2.5, 700.0)}
    #allowed_w = 15.0
    #budget = 1450.00
    #product_shopping(p_list, allowed_w, budget)
    #p_list = {"shirt": (0.13, 1200.), "trousers": (0.36, 850.),
    #"jeans": (0.3, 1300.), "shoes": (0.5, 1200.),
    #"socks": (0.15, 50.)}
    #allowed_w = 5.0
    #budget = 4200.00
    #product_shopping(p_list, allowed_w, budget)
