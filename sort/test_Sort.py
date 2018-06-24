'''
Created on Sep 23, 2017

@author: gaosh
'''
import copy
import random
import unittest

from sort.HeapSort import MaxHeap
from sort.InsertionSort import insertionSort
from sort.MergeSort import mergeSort
from sort.QuickSort import quickSort


class Test(unittest.TestCase):


    def xtestInsertionSort(self):
        lst = [random.randint(0,1000) for r in xrange(100)]         
        lst2 = copy.deepcopy(lst)
                
        print lst
        print lst2
        print 
        ret = insertionSort(lst)
        lst2.sort()
        self.assertEqual(ret,  lst2)
        
        print ret
        print lst2


    def xtestMergeSort(self):
        lst = [random.randint(0,1000) for r in xrange(100)]         
        lst2 = copy.deepcopy(lst)
                
        print lst
        print lst2
        print 
        ret = mergeSort(lst, 0, len(lst)-1)
        lst2.sort()
        self.assertEqual(ret,  lst2)
        
        print ret
        print lst2

    def xtestHeapSort(self):
        lst = [random.randint(0,1000) for r in xrange(100)]         
        lst2 = copy.deepcopy(lst)
                
        print lst
        print lst2
        print 
        heap = MaxHeap(lst)
        heap.headSort()
        
        lst2.sort()
         
        self.assertEqual(heap.array,  lst2)
        print heap.array
        print lst2
        
    def testQuickSort(self):
        lst = [random.randint(0,1000) for r in xrange(100)]         
        lst2 = copy.deepcopy(lst)
                
        print lst
        print lst2
        print 
        ret = quickSort(lst)
        lst2.sort()
        print lst
        print lst2
        self.assertEqual(lst,  lst2)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testInsertionSort']
    unittest.main()