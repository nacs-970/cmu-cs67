def lucky_name(name: str) -> bool:
    str_ = 'aeiouAEIOU'
    if name[0] in str_ or name[-1] in str_:
        if name[0] in str_ and name[-1] in str_:return False
        return True
    return False