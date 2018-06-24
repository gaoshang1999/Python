# 712. Minimum ASCII Delete Sum for Two Strings
# DescriptionHintsSubmissionsDiscussSolution
# Discuss Pick One
# Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.
# 
# Example 1:
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
# Example 2:
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d]+101[e]+101[e] to the sum.  Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
# Note:
# 
# 0 < s1.length, s2.length <= 1000.
# All elements of each string will have an ASCII value in [97, 122].

import sys
import numpy as np

class Solution(object):

    def print(self, A):
#         print(np.matrix(A))
        print("[")        
        for x in A:
            print()
            for y in x:
                print( y, end="\t")
        print("]")
    
    def minimumDeleteSum1(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        m = len(s1)
        n = len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        c = [[0] * (n + 1) for _ in range(m + 1)]
        
        self.findAllLcs(s1, s2, dp, c, 1, 1, m, n)
        return self.min
    
    def findAllLcs(self, s1, s2, dp, c, i, j, m, n):
        if j == n + 1 :
            j = 1
            i += 1
        if i == m + 1 :
            self.minV(c, s1, s2)
            return
        o1 = dp[i][j]
        o2 = c[i][j]
        if s1[i - 1] == s2[j - 1] :
            dp[i][j] = dp[i - 1][j - 1] + 1
            c[i][j] = 1
            self.findAllLcs(s1, s2, dp, c, i, j + 1, m, n)
        elif dp[i - 1][j] > dp[i][j - 1] :
            dp[i][j] = dp[i - 1][j]
            c[i][j] = 2
            self.findAllLcs(s1, s2, dp, c, i, j + 1, m, n)
        elif dp[i - 1][j] == dp[i][j - 1] :            
            dp[i][j] = dp[i - 1][j]
            c[i][j] = 2
            self.findAllLcs(s1, s2, dp, c, i, j + 1, m, n)
            
            dp[i][j] = dp[i][j - 1]
            c[i][j] = 3
            self.findAllLcs(s1, s2, dp, c, i, j + 1, m, n)
        else :
            dp[i][j] = dp[i][j - 1]
            c[i][j] = 3
            self.findAllLcs(s1, s2, dp, c, i, j + 1, m, n)
            
        dp[i][j] = o1
        c[i][j] = o2
        
    def minV(self, c, s1, s2):
        a, b = self.findIndice(c) 
        self.min = min(self.min, self.sumOfDelLetters(a, s1) + self.sumOfDelLetters(b, s2))   
        
    def sumOfDelLetters(self, a, s):
        sum = 0
        for i in range(len(a)):
            if a[i] == 0:
                sum += ord(s[i])
         
        return sum           
    
    def findIndice(self, c):
        m = len(c)
        n = len(c[0])
        a = [0] * (m - 1)
        b = [0] * (n - 1)
        i, j = m - 1, n - 1
        while (i > 0 and j > 0):
            if c[i][j] == 1:
                a[i - 1] = 1
                b[j - 1] = 1
                i, j = i - 1, j - 1
            elif c[i][j] == 2:
                i, j = i - 1, j
            else:
                i, j = i, j - 1
        return (a , b)
        


        
        
    def minimumDeleteSum2(self, s1, s2):
        self.s1 = s1
        self.s2 = s2       
        self.sumS1S2();        
        m, n = self.m, self.n
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        cs = [[0] * (n + 1) for _ in range(m + 1)]
        ws = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1] :  
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    cs[i][j] = 1                
                    ws[i][j] = ws[i - 1][j - 1] + ord(s1[i - 1])
                elif dp[i - 1][j] > dp[i][j - 1] : 
                    dp[i][j] = dp[i - 1][j] 
                    cs[i][j] = 2,
                    ws[i][j] = ws[i - 1][j] 
                elif dp[i - 1][j] < dp[i][j - 1]: 
                    dp[i][j] = dp[i][j - 1] 
                    cs[i][j] = 3,
                    ws[i][j] = ws[i][j - 1] 
                else :
#                     if ord(s1[i-1-1]) > ord(s2[j-1-1]):
#                         dp[i][j] = dp[i - 1][j] 
#                         cs[i][j] = 2
#                     else: 
#                         dp[i][j] = dp[i][j - 1] 
#                         cs[i][j] = 3
                    dp[i][j] = dp[i][j - 1] 
                    cs[i][j] = (2, 3)
                    ws[i][j] = max(ws[i - 1][j] , ws[i][j - 1] )
                          
#         self.buildLcs(cs, m, n, [])
        self.print(dp)
        self.print(cs)
        self.print(ws)
#         print(self.minValue)
        self.minValue = self.sum  - 2 * ws[i][j]
        return self.minValue
    
    def __init__(self):
        self.minValue = sys.maxsize
        
    
    def buildLcs(self, cs, i, j, lcs):
        if i == 0 or j == 0:
#             print(lcs)
            self.minValue = min(self.minValue, self.deleteValue(lcs))
#             print(self.minValue)
            return 
        if cs[i][j] == 1:
            lcs.insert(0, self.s1[i-1])
            self.buildLcs(cs, i-1, j-1, lcs)
            del lcs[0]
#         elif cs[i][j] == 2:
#             self.buildLcs(cs, i-1, j, lcs)
#         elif cs[i][j] == 3:
#             self.buildLcs(cs, i, j-1, lcs)
#         elif cs[i][j] == 4:
#             self.buildLcs(cs, i-1, j, lcs)
#             self.buildLcs(cs, i, j-1, lcs)            
        else :
            for x in cs[i][j]:
                if x == 2:
                    self.buildLcs(cs, i-1, j, lcs)
                if x == 3:
                    self.buildLcs(cs, i, j-1, lcs)
                    
    def deleteValue(self, lcs):
        print("self.sumAsscii(lcs) -> ", lcs, self.sumAsscii(lcs), self.sum1 + self.sum2 - 2 * self.sumAsscii(lcs))
        return self.sum - 2 * self.sumAsscii(lcs)
            
    def minimumDeleteSum3(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        A similar problem from LCS(Longest Common Sequence). Here We need to find the lcs which has the heaviest value        
        """        
        self.s1 = s1
        self.s2 = s2       
        self.sumS1S2();        
        m, n = self.m, self.n        

        ws = [[0] * (n + 1) for _ in range(m + 1)]
        cs = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1] :      
                    cs[i][j] = 1                       
                    ws[i][j] = ws[i - 1][j - 1] + ord(s1[i - 1])
                elif ws[i - 1][j] > ws[i][j - 1] : 
                    cs[i][j] = 2                
                    ws[i][j] = ws[i - 1][j] 
                elif ws[i - 1][j] < ws[i][j - 1]: 
                    cs[i][j] = 3                
                    ws[i][j] = ws[i][j - 1] 
                else :
                    cs[i][j] = 4                
                    ws[i][j] = max(ws[i - 1][j] , ws[i][j - 1] )
        self.print(cs)
        self.print(ws)
        return self.sum  - 2 * ws[i][j]

    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        A similar problem from LCS(Longest Common Sequence). Here We need to find the lcs which has the heaviest value        
        """        
        self.s1 = s1
        self.s2 = s2       
        self.sumS1S2();        
        m, n = self.m, self.n        

        ws = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1] :              
                    ws[i][j] = ws[i - 1][j - 1] + ord(s1[i - 1])
                else :      
                    ws[i][j] = max(ws[i - 1][j] , ws[i][j - 1] )

#         self.print(ws)
        return self.sum  - 2 * ws[i][j]

    
    def sumS1S2(self):
        self.sum1 = self.sumAsscii(self.s1)
        self.sum2 = self.sumAsscii(self.s2)
        self.sum  = self.sum1 + self.sum2 
        self.m = len(self.s1)
        self.n = len(self.s2)
    
    def sumAsscii(self, s):
        return sum( ord(x) for x in s)
    

        
    
    
s = Solution()
# s1 = "let"
# s2 = "leet"
# 
# print s.minimumDeleteSum(s1, s2)
# s1 = "sea"
# s2 = "eat"
# print s.minimumDeleteSum(s1, s2)
s1 = "elete"; s2 = "leet"
# s1 = "ab"; s2 = "ba"
print(s.minimumDeleteSum3(s1, s2))
                
            
