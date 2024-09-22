def rc1(n):
    t = n//1000
    return n >= 100000 and n <= 333333 and t != 112 and t%112 ==0 and t == n %1000
print(rc1(42))
print("---")
def f(x1,x2,n):
    d1 = (x1 // (10**n)) % 10
    d2 = (x2 // (10**n)) % 10
    if d1 > d2 and d1 > 5: return d1
    elif d2 > d1: return d2
    elif d1 == 0 and d2 == 0: return 42
    elif d1 == 0 or d2 == 0:return -10**10
    else: return 0
def rc2(x,y):
    z = 100*f(x,y,2) + 10*f(x,y,1) + f(x,y,0)
    return f(x,y,3) == 42 and z == 206
print(rc2(42,99))
print("---")
def loop(x):
    while x>0:
        print(x)
        for y in range(1,x,3):
            print(y)
        if x%3 > 0:
            print("A")
        elif x/3 > 0:
            print("B")
        x -= 4
loop(9)
print("---")
def func1(m,n):
    t = 0 
    for x in  range(m,n+1,3):
        print("x =",x);t += x
    for y in range(m,m+2):
        print("y =",y);t += y
    print(t)
    return t
func1(1,9)
print("---")
def func2(n):
    k,t = 0,0 
    while (n >= k):
        print("k =",k)
        for i in range(k):
            t += n%10 
            n //= 10 
            print(i,n%10,t)
        k+=1
    print("total =",t)
func2(1234)
print("---")
def func3(n):
    t = 0 
    for y in range(n,1,-1):
        if y%2 == 0:
            print('skip =',y)
            continue
        t += y 
        if t > 20:
            print("break =",y)
            break
    print(t)
    return t
func3(10)