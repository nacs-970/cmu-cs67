#!/usr/bin/env python
# 670510681
# Atithep Thepkij (Tun)
# Lab13_1
# 204111 Sec 002

def matrix_mult(m1:list[list[int]], m2:list[list[int]]) -> list[list[int]]:
    #min_,max_ = min(m1,m2),max(m2,m1)

    #if len(m2) >= len(m1):
    #    min_ = m1; max_ = m2
    #else:
    #    min_ = m2; max_ = m1

    #for i in 
    #r1,c1,r2,c2 = 0,0,0,0 # 1 = min | 2 = max

    ans = []
    transpose = list(zip(*m2))
    #print(min_,transpose)
    #print(transpose)
    for i in range(len(m1)):
        temp = []
        for j in range(len(transpose)):

            if len(m1[i]) != len(transpose[j]):
                return None

            #print(min_[i],transpose[j])
            temp += [sum(list(map(lambda x,y: x*y,m1[i],transpose[j])))]
        #print(temp)
        ans += [temp]
    return ans
    #print(ans)

if __name__ == "__main__":
    assert (matrix_mult([[1,2,3],[4,5,6]],[[7,8],[9,10],[11,12]])) == [[58,64],[139,154]]
    assert (matrix_mult([[1,2,3],[4,5,6]],[[7,8,5,9,3],[9,10,-3,7,13],[11,12,6,2,9]])) == [[58, 64, 17, 29, 56],[139, 154, 41, 83, 131]]
    assert (matrix_mult([[48, 59]],[[31], [37], [30]])) == None
    assert (matrix_mult([[1,2,3,4]],[[5],[6],[7],[8]])) == [[70]]
    assert (matrix_mult([[1,0,2],[-1,3,1]],[[3,1],[2,1],[1,0]])) == [[5,1],[4,2]]
    assert (matrix_mult([[21], [19], [47], [33], [1]],[[63, 1, 65, 47, 18], [75, 29, 97, 96, 3]])) == None
    print("--------------------------")
    #print(matrix_mult([[21], [19], [47], [33], [1]],[[63, 1, 65, 47, 18], [75, 29, 97, 96, 3]]))
