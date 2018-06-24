# 474. Ones and Zeroes
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.
# 
# For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.
# 
# Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.
# 
# Note:
# The given numbers of 0s and 1s will both not exceed 100
# The size of given string array won't exceed 600.
# Example 1:
# Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
# Output: 4
# 
# Example 2:
# Input: Array = {"10", "0", "1"}, m = 1, n = 1
# Output: 2
# 
# Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".

import sys

class Solution(object):
    def findMaxFormBruteForce(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        l = len(strs)
        cts = {}
        for i in range(l):
            cts[strs[i]] = self.countOnesAndZeros(strs[i])
        
        return self.helper(strs, cts, m, n, 0)
        
    def helper(self, strs, cts, m, n, k):
        l = len(strs)
        if l == 0 :
            return 0
        if m < 0 or n < 0 :
            return -1
        if m == 0 and n == 0 :
            return 0
        
        mx = 0   
        for i in range(k, l):
            s = strs[i]
            _1s, _0s = cts[s]
            strs[k], strs[i] = strs[i], strs[k]
            mx = max(mx, 1 + self.helper(strs, cts, m - _0s, n - _1s, k+1))
            strs[k], strs[i] = strs[i], strs[k]            

        return mx
        
        
    def countOnesAndZeros(self, s):
        ones = 0
        for c in s :
            if c == "1":
                ones +=1
        return (ones, len(s)-ones)
    
    
    def findMaxForm(self, strs, m, n):
        l = len(strs)
        cts = {}
        for i in range(l):
            cts[strs[i]] = self.countOnesAndZeros(strs[i])
            
        
        dp = [ [0 for _ in range(n+1)] for _ in range(m+1)]
        
#         self.pa(dp)

        for s in strs:   
            _1s, _0s = cts[s]
            for i in range(m, _0s-1,-1):
                for j in range(n, _1s-1, -1):  
                        dp[i][j] = max(dp[i][j] , dp[(i - _0s)][(j - _1s)] +1)
            self.pa(dp)             
#             for i in range(_0s, m+1):
#                 for j in range(_1s, n+1):
#                     dp[i][j] = max(dp[i][j] , dp[(i - _0s)][(j - _1s)] +1)

                      
        return dp[-1][-1]
    def pa(self, m):
        for l in m:
            print(l)  
        print()
            
#     def findMaxForm(self, strs, m, n):
#         
#         dp = [[0] * (n+1) for _ in range(m+1)]
#         
#         def count(s):
#             return sum(1 for c in s if c == '0'), sum(1 for c in s if c == '1')
#         
#         for z, o in [count(s) for s in strs]:
#             for x in range(m, -1, -1):
#                 for y in range(n, -1, -1):
#                     if x >= z and y >= o:
#                         dp[x][y] = max(1 + dp[x-z][y-o], dp[x][y])
#                         
#         return dp[m][n]
    
s = Solution()

strs = ["10", "0001", "111001", "1", "0"]
m = 5
n = 3
print(s.findMaxForm(strs, m, n))
# 
# strs = ["10", "0", "1"]
# m = 1
# n = 1
#    
# print(s.findMaxForm(strs, m, n))
# 
strs = ["10", "0001", "111001", "1", "0"]
m = 4
n = 3
print(s.findMaxForm(strs, m, n))
        