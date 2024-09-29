#!/usr/bin/env python3
# Atithep THepkij (Tun)
# 670510681
# Lab14_1
# 204111 Sec 002

def sort_date(list_x: list[str], show_steps:bool=False):
    m_th = {"ม.ค.":1,"ก.พ.":2,"มี.ค.":3,"เม.ย.":4,"พ.ค.":5,"มิ.ย.":6,"ก.ค.":7,"ส.ค.":8,"ก.ย.":9,"ต.ค.":10,"พ.ย.":11,"ธ.ค.":12}
    m_int = {1:"ม.ค.",2:"ก.พ.",3:"มี.ค.",4:"เม.ย.",5:"พ.ค.",6:"มิ.ย.",7:"ก.ค.",8:"ส.ค.",9:"ก.ย.",10:"ต.ค.",11:"พ.ย.",12:"ธ.ค."}
    size = len(list_x)
    l = [(x.split("/")) for x in list_x[:]]
    l = [ tuple([x[0],m_th.get(x[1],0),x[2]]) for x in l]
    
    # make it easier
    def convertion(d,m,y):
        return int(y) * 10000 + int(m) * 100 + int(d)

    def compare_(la,lb):
        a,b = convertion(*la),convertion(*lb)
        if a < b:
            return lb,la
        return la,lb

    for n in range(1,size):

        # insertion sort
        i = n
        while i > 0:
            l[i],l[i-1] = compare_(l[i],l[i-1])
            i -= 1

        if show_steps:
            # d/m/y
            tmp = [[x[0],m_int.get(x[1],0),x[2]] for x in l]
            print(f"{n}:", ["/".join(x) for x in tmp])

    l = [[x[0],m_int.get(x[1],0),x[2]] for x in l]
    l = ["/".join(x) for x in l]
    list_x[:] = l

if __name__ == "__main__":
    list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544']
    sort_date(list_x,show_steps=True)
    print(list_x)
    print("---")
    list_x = ['1/ธ.ค./2024', '12/ม.ค./2024']
    sort_date(list_x,show_steps=True)
    print(list_x)
    list_x = ['12/ม.ค./2024', '12/ม.ค./2024']
    #list_x = ['12/ม.ค./2024']
    sort_date(list_x)
    print(list_x)
