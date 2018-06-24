# 698. Partition to K Equal Sum Subsets
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.
# 
# Example 1:
# Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
# Output: True
# Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
# Note:
# 
# 1 <= k <= len(nums) <= 16.
# 0 < nums[i] < 10000.


class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        sm = sum(nums)
        print(sm)
        return self.integerBreak(sm//k, nums) >= k
    
    def integerBreak(self, n, arr):
        
        dp = [0] * (n+1)
        dp[0] = 1    
        
        for a in arr:
            for i in range(n, a-1, -1): 
                dp[i] += dp[i-a]
  
            print(dp)        
        
        return dp[-1]  
        
s = Solution()   
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(s.canPartitionKSubsets(nums, k))

nums = [2,2,2,2,3,4,5] ; k = 4

print(s.canPartitionKSubsets(nums, k))
