# 516. Longest Palindromic Subsequence
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.
# 
# Example 1:
# Input:
# 
# "bbbab"
# Output:
# 4
# One possible longest palindromic subsequence is "bbbb".
# Example 2:
# Input:
# 
# "cbbd"
# Output:
# 2
# # One possible longest palindromic subsequence is "bb".
import numpy as np
class Solution:
    def __init__(self):
        self.dt = set()
        self.mx = 0
    
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        def helper(str, substr, i, n):
            if i == n :
                if self.ispalidromic(substr):
                    self.mx = max(self.mx, len(substr))
            else :
                a = substr
                helper(str, a, i+1, n)
                b = substr+str[i:i+1]
                helper(str, b, i+1, n)      
                
        def helper2(str, i):  
            if i == -1:
                if self.ispalidromic(str):
                    self.mx = max(self.mx, len(str))                                
            else :
                a = str
                print(a)
                helper2(a, i-1) 
                b = str[:i]+str[i+1:]
                print(b)
                helper2(b, i-1)                
                
        def helper3(s):
            q = []
            q.insert(0, s)
            while len(q) > 0 :
                a = q.pop()
                if self.ispalidromic(a):
                    return len(a)
                for i in range(len(a)):
                    b = a[:i]+a[i+1:]
                    q.insert(0, b)
                
        def lcs(s1, s2):
            m = len(s1)
            n = len(s2)
            dp = [ [0 for _ in range(m+1)] for _ in range(n+1)]
            for i in range(1,m+1): 
                for j in range(1, n+1):
                    if s1[i-1] == s2[j-1] :
                        dp[i][j] = dp[i-1][j-1] + 1
                    elif dp[i-1][j] > dp[i][j-1] :
                        dp[i][j] = dp[i-1][j] 
                    else :
                        dp[i][j] = dp[i][j-1] 
#             print(np.matrix( dp))
            return dp[-1][-1]
     
        
        def dphelper(s):
            m = len(s)
            dp = [ [1 for _ in range(m)] for _ in range(m)]
            for j in range(1, m):
                for i in reversed(range(0, j)):    
                    if s[i] == s[j] :    
                        dp[i][j] = 2 + dp[i-1][j-1] if i + 1 <= j - 1 else 2
                    else :
                        dp[i][j] = max(dp[i+1][j], dp[i-1][j])
             
            print(np.matrix( dp))       
            return dp[-1][-1]
        
        n = len(s)
        dp = [[1] * 2 for _ in range(n)]
        for j in range(1, len(s)):
            for i in reversed(range(0, j)):
                if s[i] == s[j]:
                    dp[i][j%2] = 2 + dp[i + 1][(j - 1)%2] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j%2] = max(dp[i + 1][j%2], dp[i][(j - 1)%2])
            print(dp)
        print(dp)
        return dp[0][(n-1)%2]               

            
    def ispalidromic(self, s):
        n = len(s)
        if n == 0 or n == 1 :
            self.dt.add(s)
            return True
        elif n == 2:
            if s in self.dt :
                return True
            elif s[0] == s[-1]:
                self.dt.add(s)
                return True
            else :
                return False            
        
        else :
            if s in self.dt :
                return True
            elif s[0] == s[-1] and self.ispalidromic(s[1:-1]):
                self.dt.add(s)
                return True
            else :
                return False     

s = Solution()
t = "123"
print(s.longestPalindromeSubseq(t))
#             
s = Solution()
t = "bbbab"
print(s.longestPalindromeSubseq(t))
# # #             
s = Solution()
t = "cbbd"
print(s.longestPalindromeSubseq(t))      
# 
s = Solution()
# t = "aaaaaaaaaaaaaaaaaaaaa"
# print(len(t))
# print(s.longestPalindromeSubseq(t))  
# 
# s = Solution()
# t = "abcabcabcabc"
# print(s.longestPalindromeSubseq(t))  
# 
# t = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# print (t == t[::-1])
# print(s.longestPalindromeSubseq(t))  

