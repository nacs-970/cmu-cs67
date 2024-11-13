#!/usr/bin/env python
# 670510681
# Atithep Thepkij (Tun)
# Lab13_2
# 204111 Sec 002
# TA Film for test case

def square_matrix (list_x:list[list[int]]):

    list_x[:] = [list(filter(lambda x: type(x) == int,list_x[i])) for i in range(len(list_x))] 
    col_count = max([len(x) for x in list_x])
    max_ = max(len(list_x),col_count)
    tmp_matrix = [[0] * max_ for _ in range(max_)]

    for i in range(len(list_x)):
        for j in range(len(list_x[i])):
            tmp_matrix[i][j] = list_x[i][j]

    list_x[:] = tmp_matrix
    print(list_x[-1][-1] is tmp_matrix[-1][-1])
    return list_x

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
