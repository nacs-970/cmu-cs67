d = dict()
d['Tom'] = '555-123'
d['Jerry'] = '555-456'
print(d)
print(d['Tom'])
d['Tom'] = d['Jerry']
print(d['Tom'])
print('---')

d = {}
d = {'a':0,'b':1}
print(d)
print('---')

d1,d2 = {},{}
d1['a'] = 3;d1['b'] = 5
d2['b'] = 5;d2['a'] = 3
print(d1==d2)
print(d1,d2)
print('---')

d = [("one",1),("two",2),("three",3)];d = dict(d)
print(d)
d = dict(one=1,two=2,three=3)
print(d)
print("---")
person1 = {
    'name': 'Allan S',
    'gender': 'm',
    'age': 45,
    'siblings': ['Samuel','Ammon'],
    'Pet': None
}
person2 = dict(name="Allan s",gender='m',age=45,siblings=['Samuel','Ammon'],Pet=None)
print(person1)
print(person2)
print(person1 == person2)
print("---")
d = {'one':1,'two':2,'three':3}
print(d.keys())
print(d.values())
for i in d:
    print(i)
d['four'] = 4
del d['one']
d['five'] = 5

l = list(d.keys());print(l)
l = sorted(d.keys());print(l)
print("---")
def most_freq(a):
    max_v = None
    max_c = 0
    freq = {}
    for v in a:
        #if v in freq: c = freq[v]
        #else: c = 0
        #c += 1;
        c = 1 + freq.get(v,0) # get the values of v and default if not exist is 0
        freq[v] = c
        if c > max_c:
            max_c,max_v = c,v
    return max_v

print(most_freq([2,5,3,4,6,4,2,4,5]))
print('---')

d = {'a':1,'b':2}
print(d.items())
c = dict(map(lambda x: (x[0],x[1]**2),d.items()));print(c)
c = dict(filter(lambda x: 'a' in x[0],d.items()));print(c)
c = dict(filter(lambda x:  x[1] % 2 == 0,d.items()));print(c)
