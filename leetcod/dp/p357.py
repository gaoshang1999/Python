class Solution:
    def countNumbersWithUniqueDigits_X(self, n):
        res = 1
        for i in range(n):
                cur = 9
                for j in range(i) : 
                    cur *= 9 - j
#                     print(i, j, cur)
                res += cur
#                 print(res)
        return res
    
    def countNumbersWithUniqueDigits(self, n): 
        if n < 2:
            return pow(10, n)
        dp = [ 0 for _ in range(n+1)]
        dp[2] = 9
        
        for i in range(3, n+1):            
            dp[i] = dp[i-1] * 10 + (pow(10, i-1) - pow(10, i-2) - dp[i-1]) * (i-1)
    
        print(dp)
        return pow(10, n) - sum(dp)
s = Solution()

# for k in range(1, 15):
#     print(k, s.countNumbersWithUniqueDigits(k))
    
print(15, s.countNumbersWithUniqueDigits(15))