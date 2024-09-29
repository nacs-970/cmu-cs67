#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# 204111 Sec 002

def sort_date(list_x: list[str], show_steps:bool=False):
    m_th = {"ม.ค.":1,"ก.พ.":2,"มี.ค.":3,"เม.ย.":4,"พ.ค.":5,"มิ.ย.":6,"ก.ค.":7,"ส.ค.":8,"ก.ย.":9,"ต.ค.":10,"พ.ย.":11,"ธ.ค.":12}
    m_int = {1:"ม.ค.",2:"ก.พ.",3:"มี.ค.",4:"เม.ย.",5:"พ.ค.",6:"มิ.ย.",7:"ก.ค.",8:"ส.ค.",9:"ก.ย.",10:"ต.ค.",11:"พ.ย.",12:"ธ.ค."}
    size = len(list_x);
    l = [(x.split("/")) for x in list_x[:]]
    l = [ tuple([x[0],m_th.get(x[1],0),x[2]]) for x in l]

    def compare_(la,lb,pos=-1):
        a,b = la[pos], lb[pos]

        if a == b and pos == -3:
            return la,lb

        if a > b:
            return la,lb

        if a == b:
            compare_(la,lb,pos-1)

        return lb,la

    for n in range(1,size):
        i = n
        while i > 0:
            #print(compare_(l[i],l[i-1]))
            l[i],l[i-1] = compare_(l[i],l[i-1])
            i -= 1

        #pos -= 1
        if show_steps:
            tmp = [[x[0],m_int.get(x[1],0),x[2]] for x in l]
            print(f"{n}:", ["/".join(x) for x in tmp])

    l = [[x[0],m_int.get(x[1],0),x[2]] for x in l]
    l = ["/".join(x) for x in l]
    list_x[:] = l
import random
import datetime
def test():
    m_int = {1:"ม.ค.",2:"ก.พ.",3:"มี.ค.",4:"เม.ย.",5:"พ.ค.",6:"มิ.ย.",7:"ก.ค.",8:"ส.ค.",9:"ก.ย.",10:"ต.ค.",11:"พ.ย.",12:"ธ.ค."}
    for i in range(10):
        l = []
        for i in range(random.randint(1,5)):
            d = datetime.date.fromordinal(random.randint(1,999999))
            tmp = d.strftime("%d/%m/%y").split("/")
            l += ["/".join([tmp[0],m_int.get(int(tmp[1]),0),tmp[2]])]
        print("---")
        print(l)
        sort_date(l,show_steps=True)

if __name__ == "__main__":
    test()
    #list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544']
    #sort_date(list_x,show_steps=True)
    #print(list_x)
