print("- basic -")
sqrt = [ x**2 for x in range(10)]
print(sqrt)
print("- 2 for + condition -")
a = [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(a)
print("- method calling -")
vec = [-4,-2,0,2,4]
a = [x*2 for x in vec];print(a)
a = [x for x in vec if x >= 0];print(a)
a = [abs(x) for x in vec];print(a)
fruit = [' banana', '  loganberry',' fruit  ']
a = [x.strip() for x in fruit];print(a)
print("- storage in storage -")
a = [(x,x**2) for x in range(6)];print(a)
vec = [[1,2,3],[4,5,6],[7,8,9]]
vec = [n for row in vec for n in row];print(vec)
print("- set & dict -")
import string
s = {x for x in string.ascii_lowercase[:8]};print(s)
d = {x:[] for x in string.ascii_lowercase[:8]};print(d)
ll = ['raise', 'touch','money','rotate']
vowels = "aeiou"
d = {v:list(filter(lambda w: v in w,ll)) for v in vowels};print(d)
