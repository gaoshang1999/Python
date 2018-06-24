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
        
        
def insertionSort(list):
    for i in range(1, len(list)):
        a = list[i]
        j = i-1
        while(j>=0 and list[j] > a):
            list[j+1] = list[j]
            j=j-1
        
        list[j+1] = a
    return list
    
    
    
#Use binary search to find the right place to insert