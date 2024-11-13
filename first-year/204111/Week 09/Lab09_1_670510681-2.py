#!/usr/bin/env python3
# Atithep Thepkij (Tun)
# 670510681
# Lab09_1
# 204111 Sec 002
def patterned_message(message: str, pattern:str,n=0) -> None:
    message = message.replace(' ','')
    if len(pattern) == 1: return print('\n')
    if n > len(message)-1: n = 0


    if len(pattern) == 1:return print() 
    if len(pattern) == 1:
        if pattern[0] == '*':
            print(message[0])
        elif pattern[0] == '\n':
            print('\n')
        else:print('')
        return 0

    #if pattern[0] == '\n':
    #    print('xx')
    #    return message[n] + patterned_message(message,pattern[1:],n)
    if pattern[0] == '*':
        print(message[n],end='')
        return patterned_message(message,pattern[1:],n+1)
    if pattern[0] == ' ':
        print(' ',end='')
        return patterned_message(message,pattern[1:],n)
    if pattern[0] == '\n':
        print('\n',end='')
        return patterned_message(message,pattern[1:],n)
    #print('\n')
    #return '\n' + patterned_message(message,pattern[1:],n)
if __name__ == '__main__':
    #a = '''
    #**
    #*
    #'''
    #print(a[5]) #1-4 = '' , 5-7 = **\n
    patterned_message('123', "** *** ** ** *")
    print('############')
    #patterned_message("123", "")
    print('############')
    patterned_message("123", '''

    ''')
    print('############')
    patterned_message("123", "*")
    print('############')
    patterned_message("D and C",''' 
*************** 
******   ****** 
*************** 
''') 
    print('############')
    patterned_message("Three Diamonds!",''' 
  *     *     * 
 ***   ***   *** 
***** ***** ***** 
 ***   ***   *** 
  *     *     * 
''') 
    #assert(patterned_message("123", "** *** ** ** *")) ==  '12 312 31 23 1'
