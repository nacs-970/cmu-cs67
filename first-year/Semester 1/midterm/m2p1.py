def same_letters(str1: str, str2: str) -> bool:
    str1,str2 = str1.lower(),str2.lower()
    str1 = list(filter(lambda x: x.isalpha(), str1))
    str2 = list(filter(lambda x: x.isalpha(), str2))
    
    #max_,min_ = str2,str1
    #if len(str1) >= len(str2): max_,min_ = str1,str2
    
    ans = list(map(lambda x: x in str1,str2))
    ans2 = list(map(lambda x: x in str2,str1))
    if False in ans or False in ans2:return False
    return True
