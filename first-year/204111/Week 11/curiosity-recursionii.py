def fib(n,depth=0):
    print("  "*depth,"fib(",n,")",sep="")
    if n < 2:
        result = 1
    else:
        result = fib(n-1,depth + 1) + fib(n-2,depth +1)
    print("  "*depth,"--> ",result,sep="")
    return result
fib(5) # 3:1 time, 2:2 times, 1:3 times, 0:2 times
print("---")
def fib_memoizing(n,table=None): # Top-Down Approach
    if not table:
        table = {}
    if n in table: # prevent doing it again
        print("Hit",n)
        return table[n]
    if n == 0 or n == 1:
        result = 1
    else:
        result = fib_memoizing(n-1,table) + fib_memoizing(n-2,table)
    table[n] = result
    return result
print(fib_memoizing(5))
print("---")
def reverse(s):
    r = ""
    n = 1
    for t in s:
        print("step",n,t + r)
        r = t + r;n += 1
    return r
print(reverse("abcd"))
