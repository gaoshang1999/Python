'''
Created on Sep 23, 2017

@author: gaosh
'''
import random


class MyClass(object):
    '''
    classdocs
    '''


    def __init__(self, params):
        '''
        Constructor
        '''
        
        
def mergeSort(lst, left, right):
    
    if(left == right): return [lst[left]]
    
    mid = (left+right)/2
    
    r1 = mergeSort(lst, left, mid)
    r2 = mergeSort(lst, mid+1, right)
    
    ret  = merge(r1, r2)
    return ret
    
def merge(r1, r2):
    newLst = []
    i = 0
    j = 0
    
    while(i < len(r1) and j< len(r2)):
        if(r1[i] < r2[j]):
            newLst.append(r1[i])
            i += 1
        else:
            newLst.append(r2[j])
            j += 1            
    
    while(i < len(r1)):    
        newLst.append(r1[i])
        i += 1
        
    while(j< len(r2)):
        newLst.append(r2[j])
        j += 1                

    return newLst
