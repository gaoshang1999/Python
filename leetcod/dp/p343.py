# 343. Integer Break
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. Return the maximum product you can get.
# 
# For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
# 
# Note: You may assume that n is not less than 2 and not larger than 58.

class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [i for i in range(1, n)]
        dp = [1] * (n+1)
        if n == 2:
            return 1
        elif n == 3 :
            return 2
        
        for i in range(2, n+1):
            for a in range(1, i+1):
                dp[i] = max(dp[i], a* dp[i-a])
            print(dp)
        
        return dp[-1]
    
    def integerBreakx(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = [i for i in range(1, n)]
        return self.helper(n, arr)

    def helper(self, n, arr):  
        l = len(arr)  
        if n == 0 or n == 1 :
            return 1
        
        if n < 0:
            return 0
        
        mx = 0        
        for i in range(l):
            a = arr[i]
            mx = max(mx, self.helper(n-a, arr) * a )
        return mx
    
s = Solution()
# for i in range(2, 11):
n = 11
print(s.integerBreak(n))
n = 2
print(s.integerBreak(n))
n = 9
print(s.integerBreak(n))
n = 10
print(s.integerBreak(n))

n = 58
print(s.integerBreak(n))