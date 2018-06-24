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

# p =[7, 1, 5, 3, 6, 4]
# print s.maxProfit(p)

# p =[7, 1, 5, 3, 6, 4, 7]
# print s.maxProfit(p)

p =[7, 1, 4, 7, 0, 2, 10]
print(s.maxProfit(p))
 
# p = [7, 6, 4, 3, 1]
# print s.maxProfit(p)
#  
# p = [2,4,1]
# print s.maxProfit(p)
# 
# p = [3,2,6,5,0,3]
# print s.maxProfit(p)