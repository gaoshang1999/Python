# 416. Partition Equal Subset Sum
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# 
# Note:
# Each of the array element will not exceed 100.
# The array size will not exceed 200.
# Example 1:
# 
# Input: [1, 5, 11, 5]
# 
# Output: true
# 
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
# Example 2:
# 
# Input: [1, 2, 3, 5]
# 
# Output: false
# 
# Explanation: The array cannot be partitioned into equal sum subsets.

class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sm = sum(nums)
        if sm % 2 == 1:
            return False
        
        return self.integerBreak(sm//2, nums) == 2
        

    def integerBreak(self, n, arr):
        
        dp = [0] * (n+1)
        dp[0] = 1    
        
        for a in arr:
            for i in range(n, a-1, -1): 
                dp[i] += dp[i-a]
  
#             print(dp)        
        
        return dp[-1]            
    
s = Solution()   
nums = [1, 5, 11, 5]
print(s.canPartition(nums))

nums  = [1, 2, 3, 5]
print(s.canPartition(nums))

nums = [72,77,17,63,79,95,57,40,82,39,77,20,91,41,66,78,69,94,28,2,48,35,40,32,34,65,18,56,71,15,28,18,43,41,41,50,2,86,77,11,62,56,91,77,56,61,63,39,31,52,48,65,96,97,37,50,36,88,82,75,14,41,36,12,68,1,60,1,1,40,34,75,27,73,100,13,92,93,60,64,60,65,66,56,3,63,95,3,83,73,65,73,7,63,58,57,34,26,78,99]
print(s.canPartition(nums))

print(sum(nums))
print(len(nums))