#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab09_1
# 204111 Sec 002
def patterned_message(message: str, pattern:str,n=0,str_=[]) -> None:
    message = message.replace(' ','')
    if str_ == []: str_ = pattern.splitlines()
    if n > len(message)-1: n = 0
    
    if len(str_) == 0:
        print('\n')
        return 0
    
    # one line
    if len(str_) == 1:
        if len(pattern) == 0:
            print('\n')
            return 0
        if pattern[0] == '*':
            print(message[n],end='')
            return patterned_message(message,pattern[1:],n+1,str_)
        print(' ',end='')
        return patterned_message(message,pattern[1:],n,str_)
    
    print(str_[0])    
    return patterned_message(message,pattern,n,str_[1:])

    if len(str_[0]) == 0:
        print(' ')
        return patterned_message(message,pattern,n,str_[1:])
        
    if str_[0][0] == '*':
        print(message[n],end='')
        return patterned_message(message,pattern,n+1,str_[0][1:])
    else:
        print(' ',end='')
        return patterned_message(message,pattern,n,str_[0][1:])
    #
    if len(pattern[0]) == 1:
        if pattern == '*':
            print(message[0])
            print('')
            return message[0] + '\n'
        print('\n')
        return '\n'
    if pattern[0] == '*':
        print(message[n],end='')
        return message[n] + patterned_message(message,pattern[1:],n+1)
    if pattern[0] == ' ':
        print(' ',end='')
        return ' ' + patterned_message(message,pattern[1:],n)
    print('\n')
    return '\n' + patterned_message(message,pattern[1:],n)
if __name__ == '__main__':
    a = '''
    **
    *
    '''
    #print(a[5]) #1-4 = '' , 5-7 = **\n
    patterned_message("123", "** *** ** ** *")
    patterned_message("D and C",''' 
    *************** 
    ******   ****** 
    *************** 
    ''') 
    patterned_message("Three Diamonds!",''' 
        *     *     * 
       ***   ***   *** 
      ***** ***** ***** 
       ***   ***   *** 
        *     *     * 
    ''') 
    #assert(patterned_message("123", "** *** ** ** *")) ==  '12 312 31 23 1'
