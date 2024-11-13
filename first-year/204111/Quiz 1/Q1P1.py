def cal_area(x1,y1,x2,y2,x3,y3)->float:
    def distance(p1,q1,p2,q2): return (((p1-p2)**2)+((q1-q2)**2))**0.5 # d(p,q) p = x1,y1 q = x2,y2
    d1 = distance(x1,y1,x2,y2)
    d2 = distance(x2,y2,x3,y3)
    d3 = distance(x1,y1,x3,y3)
    s = (d1+d2+d3)/2
    return float(f"{(s*(s-d1)*(s-d2)*(s-d3))**0.5:.2f}")
    
def test():
    assert cal_area(0,5,0,9,6,7) == 12
    print("d-q")
if __name__ == "__main__":
    test()