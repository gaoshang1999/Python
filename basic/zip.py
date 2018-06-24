

def myzip(*iterables):
    # zip('ABCD', 'xy') --> Ax By
    sentinel = object()
    iterators = [iter(it) for it in iterables]
    while iterators:
        result = []
        for it in iterators:
            elem = next(it, sentinel)
            if elem is sentinel:
                return
            result.append(elem)
        yield tuple(result)
        
a = [1, 2]
b = [1, 2, 3]
c = [1, 2, 3]

for x in myzip(a, b, c):
    print(x)