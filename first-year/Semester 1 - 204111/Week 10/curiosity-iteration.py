# Iterations = loop

for i in range(2,8,-2):
    print(i)# <-- print Nothing
print('########')
def sum_1_to_n(n):
    r = 0
    for i in range(n+1):
        r += i
    return r
print(sum_1_to_n(3))
print('########')
def factorial(n):
    r = 1
    for i in range(1,n+1):
        r = r*i
    return r
print(factorial(5))
print('########')
for i in range(3):
    print(i,end='')
    i = 3
print()
for i in range(3):
    i = 3
    print(i,end='')
print()
print('########')
x = 3
ans = 0
iters_left = x
while(iters_left != 0):
    ans  += x
    iters_left -= 1
    print(str(x)+'*'+str(x)+'='+str(ans))
print('########')
def gcd(a,b):
    r = a%b
    while r != 0:
        a = b
        b = r
        r = a%b
    return b
print(gcd(246,72))
print('########')
def int_power(x,y):
    a = 1
    while y != 0:
        y -= 1
        a = a * x
        print(a,x,y)
    return a
print(int_power(2.5,3))
print('########')
def int_to_bin(x):
    base = 0
    n = 0
    div = x//2
    remainder = x%2
    while 2**n <= x:
        #print(remainder)
        #print(n)
        #print(base)
        base += remainder*(10**n)
        n += 1
        remainder = div%2
        div = div//2
    return base
print(int_to_bin(45))
print('########')
# Enumerate
print('Enumerate')
for i,l in enumerate('abcd'):
    print(i,l)

print('########')
# Loop
print('Merge_sort')
def merge_list(l_a,l_b):
    len_a = len(l_a)
    len_b = len(l_b)
    i,j = 0,0
    l_c = []
    while i < len_a and j < len_b:
        if l_a[i] < l_b[j]:
            l_c.append(l_a[i])
            i += 1
        else:
            l_c.append(l_b[j]) 
            j += 1
    if i < len_a:
        l_c.extend(l_a[i:])
    if j < len_b:
        l_c.extend(l_b[j:])
    return l_c
print(merge_list([1,3,4,5,6],[2,5,7,9,10]))
print('########')
# Recursion
def merge_list(l_a,l_b):
    if not l_a:
        return l_b
    if not l_b:
        return l_a
    if l_a[0] < l_b[0]:
        sub_task = [l_a[0]]
        sub_sol = merge_list(l_a[1:],l_b)
    else:
        sub_task = [l_b[0]]
        sub_sol = merge_list(l_a,l_b[1:])
    return sub_task + sub_sol
print(merge_list([1,3,4,5,6],[2,5,7,9,10]))
print('########')
def find_pi(sample):
    import random
    def rand_num_inrange(lo,hi):
        return lo + (hi -lo)*random.random() # random.random() aproximate 0.000000000000000... to 0.99999999999...
    def is_in_circle(x,y):
        return x**2 + y **2 <=1
    num_in_circle = 0
    for s in range(sample):
        x = rand_num_inrange(0,1)
        y = rand_num_inrange(0,1)
        if is_in_circle(x,y):
            num_in_circle += 1
    return (num_in_circle/sample) * 4
print(find_pi(100000))

