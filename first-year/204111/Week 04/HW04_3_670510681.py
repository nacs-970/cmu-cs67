#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# HW04_3
# 204111 Sec 002
# Ta พี่ตะ
def main():
    test()

# l = left, t = top, w = width, h = height
#   l,t -----l+w,t
#    |          |
#   l,t+h -- l+w,t+h 

#  topl____topr
#    |      |
#    |      |
#   botl____botr

def is_overlapped(l1:float,t1:float,w1:float,h1:float,
                  l2:float,t2:float,w2:float,h2:float) -> bool:
    # Case ไม่ทับกัน
    # x : botr1 < topl2
    if l1+w1 < l2:
        return False
    # y : botr1 < topl2
    elif t1+h1 < t2:
        return False
    # x : topl1 < botr2
    elif l1 > l2+w2:
        return False
    # y : topl1 < botr2
    elif t1 > t2+h2:
        return False

    # Case ทับกัน
    else:
        return True

def test():
    assert is_overlapped(10, 10, 100, 150, 50, 100, 150, 200) == True
    assert is_overlapped(10,10,90,90,150,90,50,90) == False
    print("Ok!")

if __name__ == "__main__":
    main()
