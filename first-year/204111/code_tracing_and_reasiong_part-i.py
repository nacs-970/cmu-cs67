for i in range(0,101):
    if (i%10 == i // 10 -1) and (i// 9 * 9 == i):
        print(i)
print("-------")
for i in range(0,101):
    a = i//13
    b = i//16
    c = i//37
    if ((a>b) and (b >= c) and (i%7 == a+b+c)):
        print(i)
print("-------")
def f(x):
    print('f',x)
    x += 1 
    return (x*x)//10
def g(x):
    print('g',x)
    x = (7*x) % 5
    return f(x+3)
x = 5
print(f(g(f(x)))+x)
print("-------")
def code_tracing1(x,y):
    print((x//10)%((y%10)**3))
    if x>y:
        return isinstance(x/10,type(x))
print(code_tracing1(137,42))
print(code_tracing1(43,731))
print("-------")
def f(z):
    return z*2 
def g(z):
    z += 1 
    return z/2 
def h(z):
    if z >3:
        return z + f(g(z))
    else:
        return g(z)
def code_tracing2(z):
    print(h(z-1))
    z *= 2 # z = z*2
    return h(z)
print(code_tracing2(3))
print("-------")
def xor1(a,b):
    res = (a and not b) or (b and not a)
    return ['xor1',[a,b],res]
def xor2(a,b):
    res = (a!=b)
    return ['xor2',[a,b],res]
def xor3(a,b):
    res = (a+b > 0)
    return ['xor3',[a,b],res]
def xor4(a,b):
    res = not a == b 
    return ['xor4',[a,b],res]
def xor5(a,b):
    res = ((a-b) != (b-a))
    return ['xor5',[a,b],res]
bool_table = [[True,False],[False,True]]
bool_table = [[True,True],[True,False],[False,True],[False,False]]
for i in bool_table:
    a,b = i[0],i[1]
    print(xor1(a,b))
    print(xor2(a,b))
    print(xor3(a,b))
    print(xor4(a,b))
    print(xor5(a,b))
    print('====')