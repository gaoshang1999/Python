# 309. Best Time to Buy and Sell Stock with Cooldown
# DescriptionHintsSubmissionsDiscussSolution
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:
# 
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
# Example:
# 
# Input: [1,2,3,0,2]
# Output: 3 
# Explanation: transactions = [buy, sell, cooldown, buy, sell]

import sys
import numpy as np
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        n = len(prices)
        
        dp=[[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            lowest = prices[i]
            highest = 0
            for j in range(i+1, n):
                if prices[j] < lowest:
                    lowest = prices[j]
                    dp[i][j] = dp[i][j-1]
                elif prices[j] - lowest > highest :
                    dp[i][j] = prices[j] - lowest
                    highest = dp[i][j]                   
                else :                    
                    dp[i][j] = dp[i][j-1]
        
        
        
        
        
        
        
#         dp=[[0 for _ in range(n)] for _ in range(n)]
#         for i in range(n):
#             for j in range(i+1, n):
#                 dp[i][j] = self.maxProfit_helper(prices[i:j+1])
                
        

        print(np.array(dp))
        print()
        
        for i in reversed(range(n)):
            for j in range(i+4, n):
                    for k in range(i+1, j-2):
                        dp[i][j] = max(dp[i][j],  dp[i][k] + dp[k+2][j])
        print(np.array(dp))                        
        return dp[0][-1]
        
    def maxProfit_recursive(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """ 
        n = len(prices)
        if n <= 1 : return 0

        mx = max(0, self.maxProfit_helper(prices))
        for i in range(1, n-1):
            (a, b) = (0, 0)
            if i + 1 < n:
                prefix = prices[0:i+1]
                a = self.maxProfit(prefix)
            
            if i + 2 < n:
                suffix = prices[i+2:]
                b = self.maxProfit(suffix) 
        
            mx = max(mx, a+b)

        return mx
    
    def maxProfit_helper(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = sys.maxsize
        highest = 0;
        n = len(prices)
        for i in range(n):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] - lowest > highest :
                highest = prices[i] - lowest
        return highest 
    
s = Solution()
prices = [1,2,3,0,2]
print( s.maxProfit(prices))

prices = [1,2,3,0,2,3]
print( s.maxProfit(prices))

prices = [1,2,3,4,10]
print( s.maxProfit(prices))

prices = [1,2,4]
print( s.maxProfit(prices))
   
   
prices = [1,4, 2 ]
print( s.maxProfit(prices))     