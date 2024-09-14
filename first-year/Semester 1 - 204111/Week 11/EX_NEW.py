def eeny_meeny(name_list: list[str], rhyme_len: int=4) -> str:
    len_x =list(map(lambda x: len(x), name_list))

    c_ = 0
    ans = [(0, len_x[0], len_x[0])]
    for i in range(len(len_x[:-1])-1):
        c_ += len_x[i]
        next_ = (c_) + len_x[i+1]
        ans += [(c_, next_, len_x[i+1])]
    print(ans,len_x)

    test_ = ''.join(name_list)
    ans += [(ans[-1][-2], len(test_), len_x[-1])]
    result = ''.join(name_list)
    c_out = 0
    c_str = 0
    while len(ans) != 1:
        if c_str > len(test_)-1: c_str = 0
        print(test_,test_[c_str])
        if test_[c_str] == '$': c_str += 1
        elif c_out == rhyme_len-1:
            if test_[c_str].isupper():
                a = list(filter(lambda x: x[0] == c_str, ans))[0]
                test_ = test_[:a[0]] + '$'*a[2] + test_[a[1]:]
                #print(test_)
                ans.remove(a)
            else:
                test_ = test_[:c_str] + '$' + test_[c_str+1:]
            c_out = 0
            c_str += 1
        else:
            c_str += 1
            c_out += 1

    ans = ans[0]
    return (''.join(name_list))[ans[0]:ans[1]]


if __name__ == '__main__':
    print(eeny_meeny(['Ann', 'John', 'Mee-neoi']))
    assert eeny_meeny(['John', 'Ann', 'Tom']) == 'John'
    assert eeny_meeny(['Ann', 'Meeneoi']) == 'Ann'
    #assert eeny_meeny(['Ann']) == 'Ann'

    assert eeny_meeny(['Ann', 'John', 'Meeneoi']) == 'Meeneoi'
    assert eeny_meeny(['Ann', 'John', 'Mee-neoi']) == 'Ann'
    assert eeny_meeny(["Atom","Ann"],5) == 'Atom'
    assert eeny_meeny(['John', 'Ann', 'Tom'],5) == 'Tom'
    x = ['Tomi', 'Maudie', 'Glad', 'Jemima'] # step 9
    print(eeny_meeny(x,9))
