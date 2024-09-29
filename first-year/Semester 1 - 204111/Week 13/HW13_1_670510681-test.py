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

    filter_ = sorted(filter_, key = lambda x: len(x), reverse = True)
    
    # find the best pattern
    ans = []
    max_len,min_weight,min_budget = 0,allowed_w,budget
    for list_ in filter_:
        wc,bc = 0,0

        for n in list_:
            wc += p_list.get(n,(0,0))[0]
            bc += p_list.get(n,(0,0))[1]

        if len(list_) < max_len:
            continue

        if len(list_) >= max_len:
            max_len = len(list_)

            if wc == min_weight and bc < min_budget:
                min_budget = bc
                ans = list_
                continue

            if wc < min_weight:
                min_weight = wc
                min_budget = bc
                ans = list_
                continue

    d = dict(map(lambda x: (x,p_list.get(x,(0,0))[0]),sorted(ans)))
    return d

def test():
    import random,string
    for i in range(2000):
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
    test()