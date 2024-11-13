#!/usr/bin/env python
# 670510681
# Atithep Thepkij (Tun)
# Lab13_2
# 204111 Sec 002
#from functools import reduce
#import copy

def square_matrix (list_x:list[list[int]]):

    #for i in range(len(list_)):
    #    temp = list(filter(lambda x: x >= 0, list_[i]))
    #    list_x += [temp]

    list_x[:] = [list(filter(lambda x: type(x) == int,list_x[i])) for i in range(len(list_x))] 
    #print(list_x)

    #print(list_x)
    #col_count = len(reduce(lambda x,y: x if len(x) > len(y) else y,list_x))
    col_count = max([len(x) for x in list_x])
    #col_count = 0
    #for i in list_x:
    #    if len(i) > col_count:
    #        col_count = len(i)
    max_ = max(len(list_x),col_count)
    #print(col_count,max_)
    #if len(list_x) == col_count:
    #    #print("\n".join((list(map(lambda x: "".join(map(str,x)),list_x)))))
    #    #print("---")
    #    #return list_x
    #    max_ = 0
    #zero = [0]
    for i in range(max_):
        #print(i)

        if i < len(list_x):
            #list_x[i] = list_x[i] + copy.deepcopy(zero)*(max_ - len(list_x[i]))
            list_x[i][:] = list_x[i] + [0 for x in range(max_ - len(list_x[i]))]
            #for x in range(max_ - len(list_x[i])):
            #    list_x[i].append(0)

        else:
            #list_x.append(copy.deepcopy(zero)*max_)
            #t = []
            #for x in range(max_):
            #    t.append(0)

            #list_x.append(t)
            list_x.append([0 for x in range(max_)])
            #print(list_x[-1][0] is list_x[-1][-1])
        #elif len_ < max_:
    #print("\n".join((list(map(lambda x: "".join(map(str,x)),ans)))))
    #print("---")
    #print(list_x)
    #return list_x

if __name__ == "__main__":
    assert (square_matrix([[2, 3, 4], [1, 2, 3]])) == [[2, 3, 4],[1, 2, 3],[0, 0, 0]]
    assert (square_matrix([[1, 2], [1, 2, 3], [1, 2], [1, 2], [1]])) == [[1, 2, 0, 0, 0],[1, 2, 3, 0, 0],[1, 2, 0, 0, 0],[1, 2, 0, 0, 0],[1, 0, 0, 0, 0]]
    assert (square_matrix([[1, 2], [3, 4], [5, 6]])) == [[1,2,0],[3,4,0],[5,6,0]]
    assert (square_matrix([[1,2,3], [1,2,3], [1,2,3]])) == [[1,2,3], [1,2,3], [1,2,3]]
    print("---------------------------")
    print(square_matrix([[1], [3]]))
    print(square_matrix([[1]]))
    print(square_matrix([[1,2,3]]))
    print(square_matrix([[1,-1]]))
    print(square_matrix([[1.0,-1]]))
    print(square_matrix([[]]))
    print(square_matrix([[1,2,3],[1]]))

    l = [[2, 3, 4], [1, 2, 3]]
    print(l)
    print(square_matrix(l))
    print(l)
    #print(square_matrix(l)[-1][0])
    #print(square_matrix(l)[-1][0] is square_matrix(l)[-1][1])
