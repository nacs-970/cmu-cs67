from random import randint

def parking_fee(d1,h1,d2,h2) -> int:
    def fee(h):
        if h == 1:return 20
        if h == 2:return 30
        if h == 3:return 40
        if h>=4 and h<=12:return 100
        if h>=13 and h<=23:return 180
        else: return 200
    # ข้ามวัน
    if d2>d1:
        # ข้ามไม่ครบวัน
        if h2<=h1:
            dh = d2-d1
            dh = (dh*24) - abs(h2-h1)
            if dh%24 == 0:
                return (dh//24)*200
            else: return ((dh//24)*200) + fee(dh%24)
        # ข้ามครบวัน
        else:
            dh = (d2-d1)
            return (dh*200)+fee(h2-h1)
    else: return fee(h2-h1)

def parking_fee_2(d1,h1,d2,h2) -> int:
    # tonnam
    def fee(h):
        if h == 1:return 20
        if h == 2:return 30
        if h == 3:return 40
        if h>=4 and h<=12:return 100
        if h>=13 and h<=23:return 180
        else: return 200
    diff_ = ((d2-d1)*24) + h2-h1
    return (diff_//24)*200 + fee(diff_%24)

def test():
    d1 = randint(1,29)
    h1 = randint(0,23)
    d2 = d1 + randint(1,29)
    h2 = randint(0,23)
    for i in range(999999):
        try:
            assert parking_fee_2(d1,h1,d2,h2) == parking_fee(d1,h1,d2,h2)
        except:
            print(d1,h1,d2,h2)
            print(f"except : {parking_fee(d1,h1,d2,h2)}, got : {parking_fee_2(d1,h1,d2,h2)} ")
            return 0
    print("$ u $")
    #assert parking_fee(1,1,1,2) == 20
if __name__ == "__main__":
    test()