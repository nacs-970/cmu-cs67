def find_mode(score_list:list[int]) -> list[int]:
    score_list = sorted(score_list) # min -> max
    range_ = range(len(score_list))
    nodupe1 = list(map(lambda x,y: x != y, score_list[1:],score_list[:-1]))
    
    score_list += ['x']
    nodupe = list(filter(lambda x: score_list[x] != score_list[x+1],range_))
    nodupe = list(map(lambda x: score_list[x],nodupe))
    print(nodupe1)
    index_ = range(len(nodupe))
    count_ = list(map(lambda x: score_list.count(x),nodupe))
    ans = list(map(lambda x: nodupe[x] if count_[x] == max(count_) else 'x',index_))
    ans = list(filter(lambda x: x != 'x',ans))
    return ans
    #count_ += ['x']
    #count_ = list(filter(lambda x: count_[x] != count_[x+1],range_))
    
    
find_mode([50,50,50,60,60])