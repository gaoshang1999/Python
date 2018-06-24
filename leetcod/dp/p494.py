# 494. Target Sum
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
# 
# Find out how many ways to assign symbols to make sum of integers equal to target S.
# 
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3. 
# Output: 5
# Explanation: 
# 
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
# 
# There are 5 ways to assign symbols to make the sum of nums be target 3.

# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.



class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        
        dt= {}
                
        return self.getV(dt, nums, n-1, S)
    
    def getV(self, dt, nums, k, S):
            if k == -1 and S == 0 :
                return 1
            elif k < 0 :
                return 0
            a = nums[k]
            if not (k, S) in dt:
                if (k-1, S-a) in dt:
                    v1 = dt[(k-1, S-a)]
                else :
                    v1 = self.getV(dt, nums, k-1, S-a)
                    dt[(k-1, S-a)] = v1
                if (k-1, S+a) in dt :
                    v2 = dt[(k-1, S+a)]
                else :
                    v2 = self.getV(dt, nums, k-1, S+a)
                    dt[(k-1, S+a)] = v2
                dt[(k, S)] = v1 + v2
            #print(dt)
            return dt[(k, S)]
    
    def findTargetSumWaysx(self, nums, S):
        def helper(nums, S, k):
            if k == -1 and S == 0 :
                return 1
            elif k < 0:
                return 0
                        
#             print(k)
            a = nums[k]
            return helper(nums, S-a, k-1) + helper(nums, S+a, k-1)
        return helper(nums, S, len(nums)-1)
    
so = Solution()    
nums = [1, 1, 1, 1, 1]
S =3

print(so.findTargetSumWays(nums, S))


nums =[0,0,0,0,0,0,0,0,1]
S =1
print(so.findTargetSumWays(nums, S))

nums =[1,2,7,9,981]
S =1000000000
print(so.findTargetSumWays(nums, S))
        
        
nums = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
S =0
print(so.findTargetSumWays(nums, S))