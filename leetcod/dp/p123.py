# 121. Best Time to Buy and Sell Stock
# DescriptionHintsSubmissionsDiscussSolution
# Discuss Pick One
# Say you have an array for which the ith element is the price of a given stock on day i.
# 
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# 
# Example 1:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# 
# max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)
# Example 2:
# Input: [7, 6, 4, 3, 1]
# Output: 0
# 
# In this case, no transaction is done, i.e. max profit = 0.

import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)    
        if n==0:
            return 0          
        dp1 = self.helper(prices)
        dp2 = self.helper2(prices)
        mx = max(dp2[-1], dp2[0])
        print(prices)        
        print(dp1)
        print(dp2)        
        for i in range(n-2):
            a = dp1[i]
            b = dp2[i+1]
            mx = max(mx, a+b)
        return mx
        
    def helper(self, prices):
        n = len(prices)
        dp1 = [0 for _ in range(n)]
        lowest = sys.maxsize
        mx = 0
        for i in range(n):
            if prices[i] < lowest:
                lowest = prices[i]
            dp1[i] = mx = max(mx, prices[i] - lowest)
            
        return dp1
    
    def helper2(self, prices):
        n = len(prices)
        dp2 = [0 for _ in range(n)]
        highest = 0
        mx = 0
        for i in range(n-1, -1, -1):
            if prices[i] > highest:
                highest = prices[i]
            dp2[i] = mx = max(mx, highest - prices[i])
        return dp2
        
    def maxProfitBruteForce(self, prices):
        n = len(prices)
        mx = 0;
        for i in range(n-1):
            a = self.maxProfitHelper(prices, 0, i)
            b = self.maxProfitHelper(prices, i, n-1)
            mx = max(mx, a+b)
        return mx
        

    def maxProfitHelper(self, prices, l, h):
        lowest = sys.maxsize
        highest = 0;
        for i in range(l, h+1):
            if prices[i] < lowest:
                lowest = prices[i]
            elif prices[i] - lowest > highest :
                highest = prices[i] - lowest
        return highest 

s = Solution()

p =[7, 1, 5, 3, 6, 4]
print( s.maxProfit(p))
print( s.maxProfitBruteForce(p))

p =[7, 1, 5, 3, 6, 4, 7]
print( s.maxProfit(p))
print( s.maxProfitBruteForce(p))

p =[7, 1, 4, 7, 0, 2, 10]
print(s.maxProfit(p))
print( s.maxProfitBruteForce(p)) 

p = [3,2,6,5,0,3]
print(s.maxProfit(p))
print( s.maxProfitBruteForce(p)) 
# p = [7, 6, 4, 3, 1]
# print s.maxProfit(p)
#  
# p = [2,4,1,5]
# print s.maxProfit(p)
# 
# p = [3,2,6,5,0,3]
# print s.maxProfit(p)


 
