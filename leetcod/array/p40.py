# 40. Combination Sum II
# DescriptionHintsSubmissionsDiscussSolution
# Discuss Pick One
# Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# 
# Each number in C may only be used once in the combination.
# 
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
# A solution set is: 
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]

import time
class Solution(object):
    def __init__(self):
        self.ret = set()
    
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s = []
        candidates.sort()
        self.helper(candidates, target, s, 0)
        return map(list, self.ret) 
        
    def helper(self, c, t, s, j):
        sm = sum(s)
        if sm > t:
            return 
        elif sm == t :            
            self.ret.add(tuple(s))
            return  
        
        for i in range(j, len(c)) :
            n = c[i]
            s.append(n)
            self.helper(c, t, s, i+1)
            s.pop()
        
        
        
# s = Solution()
# c = [10, 1, 2, 7, 6, 1, 5]
# target = 8
# print s.combinationSum(c, target)

print time.time()
c = [34,18,14,22,16,22,5,34,9,20,10,7,22,19,11,9,20,6,33,30,8,11,5,31,11,25,25,26,30,23,15,30,28,25,9,10,34,32,31,9,17,6,33,26,13,32,30,28,33,28,24,28,34,24,24,32,7,7,23,32,25,25,19,18,7,16,15]
t = 22
s = Solution()
print s.combinationSum(c, t)
print time.time()