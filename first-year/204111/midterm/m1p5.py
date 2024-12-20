import math
def median(list_a:list[int]) -> float:
    len_ = len(list_a)
    list_a = sorted(list_a)
    mid = len_//2
    if len_%2 == 1: return list_a[mid]
    return (list_a[mid] + list_a[mid-1])/2
    
if __name__ == '__main__':
    #print(median([28, 14, 13, 21, 19, 27, 23, 30, 16, 3]))
    EPSILON = 10**-3
    assert math.isclose(median([1, 2, 3]), 2, abs_tol=EPSILON)
    assert math.isclose(median([3, 2, 1, 0]), 1.5, abs_tol=EPSILON)
    print('ALL OK!')
