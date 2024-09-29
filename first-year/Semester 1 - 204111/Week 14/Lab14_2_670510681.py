#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# Lab14_2
# 204111 Sec 002

def search_event(list_: list[tuple[str]],key: str, show_steps: bool=False) -> tuple[str] | None:
    
    lo = 0; hi = len(list_) - 1
    d_m = {"Jan":1,"Feb":2,"Mar":3,"Apr":4,"May":5,"Jun":6,"Jul":7,"Aug":8,"Sep":9,"Oct":10,"Nov":11,"Dec":12}
    
    def convertion(str_):
        d,m,y = str_.split("/")
        m = int(d_m.get(m,0))
        return int(y) * 10000 + m * 100 + int(d)

    #list_ = sorted(set_,key = lambda x: convertion(x[0]))
    key = convertion(key) 

    while lo <= hi:
        mid = (lo + hi)//2
        compare = convertion(list_[mid][0])
        #print(list_[lo][0],list_[mid][0],list_[hi][0])
        if show_steps:
            print(f"{[mid]}:",list_[mid][0])
        if key == compare:
            return list_[mid]
        elif key < compare:
            hi = mid - 1
        else:
            lo = mid + 1
    return None

if __name__ == "__main__":
    list_x = [('11/Jan/1900', 'Event A'), ('5/Dec/2001', 'Event B'),('5/Dec/2002', 'Event C'), ('21/Aug/2008', 'Event D'),('9/Mar/2013', 'Event E'), ('11/Mar/2017', 'Event F'),('7/May/2019', 'Event G'), ('29/Feb/2032', 'Event H'),('9/Nov/2042', 'Event I')]
    assert search_event(list_x, '29/Feb/2032') == ('29/Feb/2032', 'Event H')
    assert search_event(list_x, '23/Aug/2008') == None
    print("---")
    list_x = [('11/Nov/1900',"A"),("12/Nov/1900","B"),("13/Nov/1900","C")]
    event = search_event(list_x, '11/Nov/1900', show_steps=True)
    print(event)
