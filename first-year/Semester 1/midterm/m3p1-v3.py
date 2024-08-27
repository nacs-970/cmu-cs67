def find_mode(score_list:list[int]) -> list[int]:
    #score_list = sorted(score_list) # min -> max
    min_,max_ = min(score_list),max(score_list)
    count_ = list(map(lambda x:score_list.count(x),range(min_,max_+1)))
    ans = list(filter(lambda x: score_list.count(x) == max(count_),range(min_,max_+1)))
    return ans

#print(find_mode([50,50,60,60]))
#print(find_mode([50,60,60]))
