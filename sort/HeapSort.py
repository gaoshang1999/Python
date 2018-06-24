'''
Created on Sep 24, 2017

@author: gaosh
'''

class MaxHeap(object):
    
    def __init__(self, lst):
        self.array = [x for x in lst]
        self.length = len(lst)
        self.buildMaxHead()        
        
    def left(self, i):
        return 2*i + 1;    
    def right(self, i):
        return 2*i + 2
    
    def parent(self, i):
        return (i-1)/2
        
    def maxHeapify(self, i):   
        l = self.left(i)
        r = self.right(i)
        
        if l <= self.size and self.array[l] > self.array[i] :
            largest = l
        else:
            largest = i
            
        if r <= self.size and self.array[r] > self.array[largest] :
            largest = r
        
        if largest != i :
            self.array[largest], self.array[i] = self.array[i], self.array[largest]
            self.maxHeapify(largest)
            
    
    def buildMaxHead(self):
        self.size = self.length - 1
        for i in xrange( (self.size -1) /2, -1, -1) :
            self.maxHeapify(i)

    def headSort(self):
        for i in xrange( self.length - 1, 0, -1) :
            self.array[0], self.array[i] = self.array[i], self.array[0]
            self.size -= 1
            self.maxHeapify(0)
            
