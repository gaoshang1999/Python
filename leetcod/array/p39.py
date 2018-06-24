# 39. Combination Sum
# DescriptionHintsSubmissionsDiscussSolution
# Discuss Pick One
# Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
# 
# The same repeated number may be chosen from C unlimited number of times.
# 
# Note:
# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# For example, given candidate set [2, 3, 6, 7] and target 7, 
# A solution set is: 
# [
#   [7],
#   [2, 2, 3]
# ]


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
            self.helper(c, t, s, i)
            s.pop()
        
        
        
s = Solution()
c =[2, 3, 6, 7] 
target = 7
print s.combinationSum(c, target)

c = [1,2]
t = 4
s = Solution()
print s.combinationSum(c, t)
 