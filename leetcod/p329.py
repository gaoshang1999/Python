
class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0 :
            return 0 
        n = len(matrix[0])
        
        dp = [ [(1, 1) for _ in range(n)]  for _ in range(m) ]
        mx = 0
        for i in range(m):
            for j in range(n):
                a = matrix[i][j]
                
                l = 1
                if j > 0:
                    if  a > matrix[i][j-1] and self.longest(dp[i][j-1]) > 0:
                        l =self.longest(dp[i][j-1]) + 1
                    elif a > matrix[i][j-1] :
                        l = 2
                    elif a < matrix[i][j-1] and self.longest(dp[i][j-1]) < 0:
                        l = self.longest(dp[i][j-1]) - 1
                    elif a < matrix[i][j-1] :
                        l = -2
                
                u = 1
                if i > 0:
                    if  a > matrix[i-1][j] and self.longest(dp[i-1][j]) > 0:
                        u = self.longest(dp[i-1][j]) + 1
                    elif a > matrix[i-1][j] :
                        u = 2
                    elif  a < matrix[i-1][j] and self.longest(dp[i-1][j]) < 0:
                        u = self.longest(dp[i-1][j]) - 1
                    elif  a < matrix[i-1][j] :
                        u = -2
                        
                dp[i][j] = (l, u)
                mx = max(mx, abs(l), abs(u))
        print(dp)       
        return mx
    
    def longest(self, dp):
        a, b = dp
        if abs(a) > abs(b):
            return a
        return b
    
s = Solution()
m = [[9,9,4],[6,6,8],[2,1,1]]
a = s.longestIncreasingPath(m)
print(a)


m = [[7,8,9],[9,7,6],[7,2,3]]
a = s.longestIncreasingPath(m)
print(a)
