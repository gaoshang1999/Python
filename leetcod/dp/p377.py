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


class Solution:
    def combinationSum4_recursive(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < 0 :
            return 0
        elif target == 0:
            return 1
        
        s = 0
        for t in nums:
            s += self.combinationSum4(nums, target - t)
        return s
    
    def combinationSum4(self, nums, target):
        if target <= 0 : return 0
        dp = [0 for _ in range(target+1)]
        dp[0] = 1
        for i in range(1, target+1):
            for a in nums:
                if i - a >= 0 :
                    dp[i] += dp[i - a]

        print(dp) 
        return dp[-1]   
        
s = Solution()        
nums = [1, 2, 3]
target = 4
print(s.combinationSum4(nums, target))

nums =[4,2,1]
target = 32
print(s.combinationSum4(nums, target))