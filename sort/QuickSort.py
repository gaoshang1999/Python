'''
Created on Sep 28, 2017

@author: gaosh
'''
import random


def partition(lst, l, r):
    if l == r : return l
    pivot = lst[l]
    i = l
    j = r
    while(i<j):
        while(i<j and lst[j]>=pivot): j-=1
        lst[i] = lst[j]
        while(i<j and lst[i]<pivot): i+=1
        lst[j] = lst[i] 
    lst[i] = pivot
    return i
    
def _quickSort(lst, l, r):
    if(l<r):
        m = partition(lst, l, r)
        _quickSort(lst, l, m-1)
        _quickSort(lst, m+1, r)
 
def quickSort(lst):
    _quickSort(lst, 0, len(lst)-1)

 
#see Introduce to Algorithm, 3rd, p171
def _partition(A, p, r):
    x = A[r]
    i = p -1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]        
    return i+1
        
lst = [random.randint(0,100) for r in xrange(5)]         
print lst
i = _partition(lst, 0, len(lst)-1)
print i
print lst