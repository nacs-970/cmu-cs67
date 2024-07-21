def parking_fee(d1,h1,d2,h2) -> int:
    def fee(h):
        if h == 1:return 20
        if h == 2:return 30
        if h == 3:return 40
        if h>=4 and h<=12:return 100
        if h>=13 and h<=23:return 180
        else: return 200
    
    if d2>d1:
        if h2<=h1:
            dh = d2-d1
            dh = (dh*24) - abs(h2-h1)
            if dh%24 == 0:
                return (dh//24)*200
            else:
                return ((dh//24)*200) + fee(dh%24)
        else:
            dh = (d2-d1)
            return (dh*200)+fee(h2-h1)
    else: 
        return fee(h2-h1)