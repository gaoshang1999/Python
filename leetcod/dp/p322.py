# 322. Coin Change
# DescriptionHintsSubmissionsDiscussSolution
# DiscussPick One
# You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
# 
# Example 1:
# coins = [1, 2, 5], amount = 11
# return 3 (11 = 5 + 5 + 1)
# 
# Example 2:
# coins = [2], amount = 3
# return -1.
# 
# Note:
# You may assume that you have an infinite number of each kind of coin.

import sys
import numpy as np

class Solution:
    def __init__(self):
        self.min = sys.maxsize    
    def coinChange2(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        self.helper(coins, amount, 0, 0)
        
        if self.min == sys.maxsize :
            return -1
        return self.min
        
        
            
    def helper(self, coins, amount, k, s):
        n = len(coins)
        if k == n:
            if amount == 0 :
                self.min = min(self.min, s)
            return
        c = coins[k]
        for i in range(amount//c+1):
            self.helper(coins, amount-c*i, k+1, s+i)    
   
    
    def _get_change_making_matrix(self,set_of_coins, r):
        m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    
        for i in range(r + 1):
            m[0][i] = i
    
        return m

    def coinChange3(self,coins, n):
        """This function assumes that all coins are available infinitely.
    
        n is the number to obtain with the fewest number of coins.
    
        coins is a list or tuple with the available denominations."""
    
        m = self._get_change_making_matrix(coins, n)
    
        for c in range(1, len(coins) + 1):
    
            for r in range(1, n + 1):
    
                # Just use the coin coins[c - 1].
                if coins[c - 1] == r:
                    m[c][r] = 1
    
                # coins[c - 1] cannot be included.
                # Use the previous solution for making r,
                # excluding coins[c - 1].
                elif coins[c - 1] > r:
                    m[c][r] = m[c - 1][r]
    
                # coins[c - 1] can be used.
                # Decide which one of the following solutions is the best:
                # 1. Using the previous solution for making r (without using coins[c - 1]).
                # 2. Using the previous solution for making r - coins[c - 1] (without using coins[c - 1]) plus this 1 extra coin.
                else:
                    m[c][r] = min(m[c - 1][r], 1 + m[c][r - coins[c - 1]])
                    
        print(m[0])
        print(m[1])
        print(m[2])
#         self.pa(m)           
    
        return m[-1][-1]
    
    def coinChange(self,coins, n):      
        dp = [ n+1 ] * (n+1)        
        dp [ 0 ] = 0
        
        for i in range(1, n+1) :
            for c in coins:
                if c <= i :
                    dp[i] = min(dp[i], dp[i-c]+1)
                
      
        if dp[n] > n:
            return -1
        else :
            return dp[n]
                    
        
        
#         if n == 0 :
#             return 0        
#         
#         for c in coins:
#             mn = min(mn, self.coinChange(coins, n-c)  + 1 ) 
#             
#         return mn
        
        
    
    def pa(self, m):
        for l in m:
            print(l)    
        
s = Solution()        
coins = [1, 2, 5]
amount = 11
# 
print (s.coinChange(coins, amount))
#         
#         
coins = [2]
amount = 3
print (s.coinChange(coins, amount))        

coins = [186,419,83,408]
amount = 6249
  
print (s.coinChange(coins, amount))      

coins = [2, 3]
amount = 13
 
print (s.coinChange(coins, amount))        

coins = [3, 2]
amount = 13
 
print (s.coinChange(coins, amount))        


coins = [3, 2]
amount = 0
 
print (s.coinChange(coins, amount))   
 


