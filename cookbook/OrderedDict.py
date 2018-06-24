
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}

print(d.items())
print(repr(d.items()))

from collections import OrderedDict
d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4
# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])
    
import copy
    
a = [1, 2, 3]
b = copy.copy(a)
print(a, b)
b.append(4)
print(a, b)