def func(x):return 10*x + 42
func2 = lambda x:10*x+42
print(func(5))
print(type(func2))
print(func2(5))
print('#####')
def longest_word(*args): # *variable == รับได้หลายตัว / แตกตัว
    if len(args) == 0:
        return None
    ans = args[0]
    for word in args:
        if len(word) > len(ans):
            return word
    return ans

print(longest_word('this','is','really','nice'))
my_word = ['this','is','really','nice']
print(longest_word(my_word))
print(longest_word(*my_word))
print('#####')
def f(x=1,y=2):return x,y
print('(x, y)')
print(f())
print(f(3))
print(f(y=3))
print('#####')
def parrot(v,s='A s',act='Vo',t='Nb'):
    print('t p w',act,end=' ')
    print('i y p',v,' v t i.')
    print(' l p, t',t)
    print('i\'s',s,'!')
parrot(1000)
parrot(v=1000)
parrot(v=1000,act='VOOOM')
parrot(act='VOOOM',v=1000)
parrot(123,456,789)
# parrot() missing a required
