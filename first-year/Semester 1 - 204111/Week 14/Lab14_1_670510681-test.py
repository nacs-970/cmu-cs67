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
    
def sort_date2(list_x: list[str], show_steps: bool=False):
    month = {'ม.ค.': 1, 'ก.พ.': 2, 'มี.ค.': 3, 'เม.ษ.': 4,
             'พ.ค.': 5, 'มิ.ย.': 6, 'ก.ค.': 7, 'ส.ค.': 8,
             'ก.ย.': 9, 'ต.ค.': 10, 'พ.ย.': 11, 'ธ.ค.': 12,}
    day = list(map(lambda x: x.split('/'), list_x))
    # [['11', 'ม.ค.', '2643'], ['5', 'ธ.ค.', '2542'], ['19', 'ม.ค.', '2546'], ['11', 'ก.ย.', '2544']]
    
    solution = list(map(lambda x: [int(x[0]), month[x[1]], int(x[-1])],day))
    # [[11, 1, 2643], [5, 12, 2542], [19, 1, 2546], [11, 9, 2544]]

    cal = list(map(lambda x: (((x[-1]*12)+x[1])*31)+x[0],solution))
    # [983238, 946001, 947162, 946658]

    dic = dict()
    for i in range(len(list_x)):
        dic[cal[i]] = list_x[i]
    # {983238: '11/ม.ค./2643', 946001: '5/ธ.ค./2542', 947162: '19/ม.ค./2546', 946658: '11/ก.ย./2544'}

    
    size = len(cal)
    text = cal[:] 

    for i in range(1, size): 
        j = i
        while j > 0 and text[j] < text[j-1]:
            text[j], text[j-1] = text[j-1], text[j] 
            j -= 1

        list_x[:] = list(map(lambda x: dic[x], text))
        if show_steps == True:
            print(str(i)+':',list_x[:])


def test():
    import random
    import copy
    m_int = {1:"ม.ค.",2:"ก.พ.",3:"มี.ค.",4:"เม.ย.",5:"พ.ค.",6:"มิ.ย.",7:"ก.ค.",8:"ส.ค.",9:"ก.ย.",10:"ต.ค.",11:"พ.ย.",12:"ธ.ค."}
    for i in range(10):
        l = []
        for j in range(random.randint(1,10)):
            l += [str(random.randint(1,28)) + "/" + m_int[random.randint(1,12)] + "/" + str(random.randint(0,9999))]
        l2 = copy.deepcopy(l)
        try:
            sort_date2(l2,show_steps=True)
            sort_date(l,show_steps=True)
            assert l2 == l
        except:
            print(l)
            print(l2)
            return 0
    print("date ;)")

if __name__ == "__main__":
    list_x = ['11/ม.ค./2643', '5/ธ.ค./2542', '19/ม.ค./2546', '11/ก.ย./2544']
    test()
