
DEBUG = False

def skip_double(list_a):
    
    # one line
    #return list(map(lambda x: list_a[::-1][x]*2 if x%2 == 1 else list_a[::-1][x],list(range(len(list_a)))[::-1]))
    
    # start from behind
    range_ = list(range(len(list_a)))[::-1]
    list_re = list_a[::-1]
    
    def comp_(list_,n):
        if n%2 == 1:return list_[n]*2
        else: return list_[n]
    
    # double only odd index
    #ans = list(map(lambda x: comp_(list_re,x),range_))
    ans = list(map(lambda x: list_re[x]*2 if x%2 == 1 else list_re[x],range_))
    
    
    if DEBUG == True: print(ans)
    return ans

if __name__ == "__main__":
    skip_double([1,1,1,1,1])
    skip_double([1,1,1,1])
    skip_double([1,1])
    skip_double([1])