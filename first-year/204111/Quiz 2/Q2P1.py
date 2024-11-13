DEBUG = True

def replace_in_range(text,start,stop,old,new):
    len_ = len(text)
    
    # start and stop out of range
    if start < -len_ : start = 0
    if stop > len_: stop = len_
    
    #text_lower = text.lower()
    #str_ = text_lower[start:stop].replace(old,new)
    
    #str_ = text[start:stop].replace(old,new)
    
    # replace method
    str_ = text[start:stop].lower().replace(old,new)
    str_ = text[:start] + str_ + text[stop:]
    
    def replace_(text,change,index_):
        if text[index_].islower():return change[index_]
        elif text[index_].isupper():return change[index_].upper()
        else:return text[index_]
        
    range_ = list(range(len(text)))
    ans = list(map(lambda x: replace_(text,str_,x), range_))
    ans = "".join(ans)
    
    if DEBUG == True:print(ans)
    return ans
if __name__ == "__main__":
    replace_in_range("Happy Birthday",-14,-1,"h","i")