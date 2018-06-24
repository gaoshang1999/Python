import random
a = [1 , 2, 3]

def f(a):
    a.append(4)
    
f(a)
# print(a)



# A = [ random.randint(0,9) for _ in range(10)]
# print(A)

def intersecttions(A, B, C):
    for a in A:
        if a in B and a in C:
            yield a
#             return True
    return None

A = [ random.randint(0,10) for _ in range(11)]
print(A)
B = [ random.randint(0,10) for _ in range(11)]
print(B)
C = [ random.randint(0,10) for _ in range(11)]
print(C)

def find_intersections():
    return list(intersecttions(A, B, C)) #and intersecttions(B, A, C)  and intersecttions(C, B, A) 

def find_intersections_2():
    a = set(A)
    b = set(B)
    c = set(C)
    print(a & b & c )
    return   (a & b & c) 
    
    
a = find_intersections()
print(a)

b = find_intersections_2()
print(b)

evens = [a for i, a in enumerate(A) if i % 2==0 and a % 2 == 0]
print(evens)

