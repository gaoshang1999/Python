def squares(n=10):
    print ('Generating squares from 1 to %d' % (n ** 2) )
    for i in range(1, n + 1):        
        yield i ** 2
        
gen = squares()

for x in gen:
    print(x)
    
    
def f():
    a = 5
    b = 6
    c = 7
    return a, b, c #{'a' : a, 'b' : b, 'c' : c}

a, b, c = f()
print(a, b, c)

a = []
def func():
    for i in range(5):
        a.append(i)
        
func()
print(a)

import  random
A = { random.randint(0,10) for _ in range(11)}
print(A)