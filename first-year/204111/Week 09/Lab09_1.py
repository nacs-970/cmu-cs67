#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab09_1
# 204111 Sec 002
def patterned_message(message: str, pattern:str,n=0) -> None:
    if not pattern: # empty string is False; not(False)
        return 

    message = message.replace(' ','')

    n = n%len(message)
    #if n > len(message)-1: n = 0

    if pattern[0] == '*':
        print(message[n],end='')
        patterned_message(message, pattern[1:], n+1)
    else:
        print(pattern[0],end='')
        patterned_message(message, pattern[1:], n)

if __name__ == '__main__':
    a = '''
    **
    *
    '''
    a = '******'
    b = '''
1
2
3
'''
    #print(a[5]) #1-4 = '' , 5-7 = **\n
    #patterned_message("123", "** *** ** ** *")
    #patterned_message("123", "")
    #patterned_message("123", '''

    #''')
    #patterned_message("123", "*")
    patterned_message(a,b)
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
