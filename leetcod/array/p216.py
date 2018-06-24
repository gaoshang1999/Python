# 216. Combination Sum III
# DescriptionHintsSubmissionsDiscussSolution
# Discuss Pick One
# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
# 
# 
# Example 1:
# 
# Input: k = 3, n = 7
# 
# Output:
# 
# [[1,2,4]]
# 
# Example 2:
# 
# Input: k = 3, n = 9
# 
# Output:
# 
# [[1,2,6], [1,3,5], [2,3,4]]

import time
class Solution(object):
    def __init__(self):
        self.ret = set()
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = [i for i in range(1, 10)]
        return self.combinationSum(candidates, n, k)
    
    def combinationSum(self, candidates, target, k):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        s = []
        candidates.sort()
        self.helper(candidates, target, s, 0, k)
        return map(list, self.ret) 
        
    def helper(self, c, t, s, j, k):
        sm = sum(s)
        l = len(s)
        if sm > t or l>k :
            return 
        elif sm == t and l ==k :            
            self.ret.add(tuple(s))
            return  
        
        for i in range(j, len(c)) :
            n = c[i]
            s.append(n)
            self.helper(c, t, s, i+1, k)
            s.pop()
        
        
        
# s = Solution()
# c = [10, 1, 2, 7, 6, 1, 5]
# target = 8
# print s.combinationSum(c, target)

s = Solution() 
k = 3
n = 7
print s.combinationSum3(k, n)

s = Solution()
k = 3
n = 9
print s.combinationSum3(k, n)
