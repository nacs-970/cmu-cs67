DEBUG = True

def replace_in_range(text,start,stop,old,new):
    # short
    str_=text[start:stop].replace(old,new) # lower case
    str_=str_.replace(old.upper(),new.upper()) # upper case
    ans = text[:start] + str_ + text[stop:]
    return ans


    len_ = len(text)
    # if string index[start and stop] out of range will use 0 (start),-1 (stop) automatically
    
    # split method
    str_ = text[start:stop].split(old)
    str_ = text[:start] + new.join(str_) + text[stop:]
    print(str_)
    
    def replace_(text,change,index_):
        if text[index_].islower():return change[index_]
        elif text[index_].isupper():return change[index_].upper()
        else:return text[index_]
        
    range_ = list(range(len_))
    ans = list(map(lambda x: replace_(text,str_,x), range_))
    ans = "".join(ans)
    
    if DEBUG == True:print(ans)
    return ans
if __name__ == "__main__":
    replace_in_range("Happy Birthday",0,14,"h","i")