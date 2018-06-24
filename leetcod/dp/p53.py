class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        sm = [0 for _ in range(n+1)]
        
        for i in range(n):
            sm[i+1] = sm[i] + nums[i]
        
        print(sm)    
        mx = max(sm[1:])
        
        for i in range(1, n+1):
            for j in range(i+1, n+1):
                mx = max(mx, sm[j]-sm[i])

        return mx;
     
     
    def maxSubArray2(self, nums ):
        def helper(nums, i, j):
            n = j - i + 1
            if n == 1:
                return nums[i]         
            else:
                sm = max( sum(nums[i:j+1]), helper(nums, i+1, j), helper(nums, i, j-1))
                return sm
        return helper(nums, 0, len(nums)-1)
    
    
    def maxSubArray3(self, nums ):
        n = len(nums)
        dp = [0 for _ in range(n)]
        dp[0] = nums[0];
        mx = dp[0];
        
        for i in range(1, n):
            print(dp)
            dp[i] = nums[i] + max(dp[i - 1], 0)
            mx = max(mx, dp[i]);
                
        return mx;
    
s = Solution();
nums = [-1]
print(s.maxSubArray(nums))
print(s.maxSubArray2(nums))
print(s.maxSubArray3(nums))

nums = [-2, -1]
print(s.maxSubArray(nums))
print(s.maxSubArray2(nums))
print(s.maxSubArray3(nums))

nums = [-2,1,-3,4,-1,2,1,-5,4] 
print(s.maxSubArray(nums))
print(s.maxSubArray2(nums))
print(s.maxSubArray3(nums))