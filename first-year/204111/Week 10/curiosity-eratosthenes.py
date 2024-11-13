def eratosthenes(f,l):
    prime = 2
    prime_list = [2]
    lo,hi = min(f,l),max(f,l)

    list_ = list(range(2,hi+1))
    list_ = list(filter(lambda x: x%prime != 0,list_))

    #while list_ != []:
    while prime**2 <= hi: # when x can't divied others mean number is less than sqrt(x) mean x is prime
        #print(prime_list)
        prime_list.append(list_[0])
        prime = list_[0]
        list_ = list(filter(lambda x: x%prime != 0,list_))

    ans = prime_list+list_

    #return list(filter(lambda x: x>=lo,ans))
    while ans[0] < lo:
        ans = ans[1:]
    return ans


print(eratosthenes(3458,1000))
