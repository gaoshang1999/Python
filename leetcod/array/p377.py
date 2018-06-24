# 377. Combination Sum IV
# DescriptionHintsSubmissionsDiscussSolution
# Discuss Pick One
# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
# 
# Example:
# 
# nums = [1, 2, 3]
# target = 4
# 
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
# 
# Note that different sequences are counted as different combinations.
# 
# Therefore the output is 7.


class Solution(object):
    def __init__(self):
        self.ret = set()
        self.n = 0
        
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
 
        return self.integerBreak_noRepeat( target, nums)
    
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        
#     def helper(self, c, t, s):
#         sm = sum(s)
#         if sm > t:
#             return 
#         elif sm == t :            
#             self.n +=1
#             return  
#         
#         for n in c :           
#             s.append(n)
#             self.helper(c, t, s)
#             s.pop()
        
    def integerBreak_noRepeat(self, n, arr):        
        def helper(n, arr, j, ret):  
            l = len(arr)  
            if n == 0 :
                print(ret)
                return 1
            
            if n < 0 or j == l:
                return 0
            
            c = 0        
            for i in range(j, l):
                a = arr[i]
                ret.append(a)
                c += helper(n-a, arr, j+1, ret)
                ret.pop()
            return c
    
        return helper(n, arr, 0, [])        
        
s = Solution()
c =[1, 2, 3]
target = 4
print ( s.combinationSum4(c, target))

# c = [1,2]
# t = 4
# s = Solution()
# print s.combinationSum(c, t)
 