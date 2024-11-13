#!/usr/bin/env python
# 670510681
# Atithep Thepkij (Tun)
# HW13_1
# 204111 Sec 002
# TA Film test case

def product_shopping(p_list: dict[str, tuple[float, float]],allowed_w: float, budget: float) -> dict[str, float]:
    # 0 < budget <= 10000
    # 5 <= allowed_w <= 1000

    # power set
    set_ = [[]]
    list_ = list(p_list.keys())

    for i in list_:
        q = map(lambda x: x + [i],set_.copy())
        set_ += q

    # filter exceed allowed_w and budget
    filter_ = []
    for list_ in set_:
        wc,bc = 0,0

        for n in list_:
            wc += p_list.get(n)[0]
            bc += p_list.get(n)[1]

        if wc > allowed_w or bc > budget:
            continue

        filter_.append(list_)

    #print(filter_)
    filter_ = sorted(filter_, key = lambda x: len(x), reverse = True)
    
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

        if len(list_) < max_len:
            continue

        if len(list_) >= max_len:
            max_len = len(list_)
            #print("hit")
            #print(list_,wc,bc)

            if wc == min_weight and bc < min_budget:
                #print(list_,wc,bc)
                min_budget = bc
                ans = list_
                continue

            if wc < min_weight:
                #print(list_,wc,bc)
                min_weight = wc
                min_budget = bc
                ans = list_
                continue

        #ans = sorted(ans)
    d = dict(map(lambda x: (x,p_list.get(x,(0,0))[0]),sorted(ans)))
    #print(d)
    return d
                #if bc < min_budget:
                #print(list_,wc,bc)
                    #print(ans)

if __name__ == "__main__":
    assert product_shopping({"table": (5, 900.), "chair": (0.4, 450.),"pillow": (3.5, 1200), "stool": (0.3, 300.0)},25.0,2500.00) == {'stool': 0.3,'chair': 0.4,'pillow': 3.5}
    assert product_shopping({"chair": (0.4, 450.0), "pillow": (3.5, 315.0),"stool": (0.3, 300.0), "closet": (2.5, 700.0)}, 15.0,1450.00) == {'stool': 0.3,'chair': 0.4,'closet': 2.5}
    assert product_shopping({"a":(0.1,10)},100.0,100.0) == {'a': 0.1}
    assert product_shopping({"a":(0.1,10)},100.0,1.0) == {}
    assert product_shopping({"shirt": (0.13, 1200.), "trousers": (0.36, 850.),"jeans": (0.3, 1300.), "shoes": (0.5, 1200.),"socks": (0.15, 50.)},5.0,4200.00) == {'jeans': 0.3, 'shirt': 0.13, 'socks': 0.15, 'trousers': 0.36}
    assert product_shopping({'j': (43, 83), 'b': (68, 95), 'f': (35, 12), 'g': (45, 58), 'd': (75, 36), 'c': (18, 55), 'x': (92, 80), 'i': (84, 98), 'm': (55, 76), 'q': (78, 38), 'w': (1, 48), 'v': (34, 47), 'l': (0, 86)},67,96) == {'w': 1, 'v': 34}
    #p_list = {"a":(1,1.), "b":(1,0.9)};allowed_w = 1; budget = 10.00
    #print(product_shopping(p_list, allowed_w, budget))
    #p_list = {"a":(1,0.5), "b":(1,1.)};allowed_w = 1; budget = 10.00
    #print(product_shopping(p_list, allowed_w, budget))
    #p_list = {"a":(1,1.), "b":(1,1.), "c":(1,1.), "d":(1,1.)};allowed_w = 4; budget = 10.00
    #print(product_shopping(p_list, allowed_w, budget))
    #p_list = {"table": (6, 120), "banana": (3.0, 35.50), "cucumber": (4.0, 42.00)}; allowed_w = 15; budget = 175
    #print(product_shopping(p_list, allowed_w, budget))
