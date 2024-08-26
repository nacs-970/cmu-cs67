def find_mode(score_list:list[int]) -> list[int]:

    score_list = sorted(score_list) # min -> max

    def remover(list_):
        if len(list_) == 1:return [list_[0]]
        if list_[0] != list_[1]: return [list_[0]] + remover(list_[1:])
        return remover(list_[1:])

    nodupe = remover(score_list)
    index_ = range(len(nodupe))

    count_ = list(map(lambda x: score_list.count(x),nodupe))
    def max_(list_):
        num = score_list.count(list_[0])
        max_c = max(count_)
        if len(list_) == 1 and num == max_c:return [list_[0]]
        if len(list_) == 1 and num != max_c:return []
        if num == max_c:return [list_[0]] + max_(list_[1:])
        return max_(list_[1:])
    
    return max_(nodupe)
