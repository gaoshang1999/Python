'''
Created on Oct 20, 2017

@author: gaosh
'''
import copy

class SubSet(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
     
    def subset(self, L):   
        n = len(L)
        if n ==0 :
            return []
        elif n == 1:
            return [[], L[:]]
        else:
            first_half = self.subset(L[:-1])
            last = L[-1]
            second_half = copy.deepcopy(first_half) 
            for t in second_half:
                t.append(last)
 
            first_half.extend(second_half)  
             
            return first_half
 
    def subset2(self, L):
        def _subset(L, level, ss, ret):
            n = len(L)
            if level == n:
                ret.append(copy.deepcopy(ss))
            else:
                a = L[level]                
                _subset(L, level+1, ss, ret)
                ss.append(a)
                _subset(L, level+1, ss, ret)
                ss.pop()
        
        r = []
        _subset(L, 0, [], r)
        return  r
        
L = [0, 1]       
s = SubSet();
print s.subset(L)      

print s.subset2(L)    