# set method
# s.copy() : shallow copy
# s.clear() : remove all elements
# s.add() : add to s
# s.remove() : remove from s raise KeyError if not present
# s.discard() : same as remove but no raise
# s.issubset(t) s <= t s.issuperset(t)  s>= t s.union(t) s|t intersection s&t symmetric_difference s^t
# s.update(t) s |= t / s = s|t intersection_update s &= t 


s = {2,3,5,7,9}
print(3 in s)
print(4 in s)
for i in range(10):
    if i not in s:
        print(i,end ="")
print()
print("---")

# collection type no order
s = set([2,4,8])
print(s)
for i in s:
    print(i,end="")
print()

s = { x*7 for x in range(10) }
print(s)
s = { x for x in range(10) }
print(s)
print("---")
# no duplicate
s = set([2,2,2])
print(s)
print(len(s))

print("---")

# only work with immutable
a = [1,2,3]
#s = set([a]) # list(list(1,2,3))
s = set(a)
print(a, "list")

a = 1,2,3
print(set(a), "tuple")
print(set(tuple(a)), "tuple in tuple")
print(set(a,), "same as above")

print("---")

s = set("zhonguo")
print(s)

print("---")
import time
n = 10000000
l = list(range(2,n+1,2))
def count_member(c,n,set_=False):
    a = c 
    if set_: a = set(c)
    start = time.time()
    count = 0
    for i in range(n+1):
        if i in a:
            count += 1
    elapesed = time.time() - start # end - start
    print(f'count: {count} time: {elapesed:0.5f} type: {type(a)}')
count_member(l,n)
count_member(l,n,True)

print("---")

def repeats(a):
    seen = set()
    seen_again = set()

    for element in a:
        if element in seen:
            seen_again.add(element)
        seen.add(element)

    return sorted(list(seen_again))
print(repeats([2,5,3,4,6,4,2]))
