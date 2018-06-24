'''
Created on Sep 25, 2017

@author: gaosh
'''
import random
import string

# print type(5/3)
# print type(5%3)

#dead loop
# a = [1]
# for x in a:
#     print x
#     a.insert(-1, x )
    
    
# for n in range(2, 100):
#      for x in range(2, n):
#          if n % x == 0:
#              print n, 'equals', x, '*', n/x
#              break
#      else:
#          # loop fell through without finding a factor
#          print n, 'is a prime number'

# while True:
#     print random.randint(0,1000)
#     pass


# def a():
#     1 
# 
# x = 10
# def b():
#     global x
#     x = 1
# 
# b()
# print x
#     
# 
# print b
# print a()
    
# def f(a, L=[]):
#     L.append(a)
#     return L
# 
# print f(1)
# print f(2)
# print f(3)


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print "-- This parrot wouldn't", action,
    print "if you put", voltage, "volts through it."
    print "-- Lovely plumage, the", type
    print "-- It's", state, "!"
    
# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


def my_function():
     """Do nothing, but document it.

     No, really, it doesn't do anything.
     xxxx
     
     xxx
     
     """
     pass

# print my_function.__doc__


# l = lambda x, y, z: (a = x + y, return a * a )
# 
# print l( 1, 2, 5)

# f = lambda i: 1 if i==0 or i==1 else f(i-1)+f(i-2)
# print f(3)

# t = lambda a, b: [(0, 9), (2, 3)][a<4][b>3]
# print t(0, 7)

class A:
    def __init__(self, v):
        self.v = v
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
    
a = A(1);
b = A(1);

# print a 
# print b
# print a == b      
# print a < b
# def f():
#     x += 1
#     print(x)
# 
# x = 5;
# f()
# print(x)

# t = (1, 2.4, "aaa")
# print t[1:3]
# 
# print 5.0/2
# print 5.0//2
# 
# print 5 * 2
# print 5 ** 2

# def f():
#     return (1, "aaa")
# 
# (a, b) = f()
# print a
# print b

# a =(1, 3, "b")
# b = a[:]
# 
# print a
# print b
# print a == b
# 
# c = [1, 3, 5]
# d = c[:]
# d.extend([7, 9])
# print c #[1, 3, 5]
# print d #[1, 3, 5, 7, 9]

a = {}

a[1] =  0 or 1
a[1] += 1;
print a[1]
    