class Solution:
    def isSubsequence_old(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        m = len(s)
        n = len(t)
        dp = [ [0 for _ in range(n+1)] for _ in range(m+1)]
        
        for i in range(1, m+1):
            for j in range(1, n+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else :
                    dp[i][j] = dp[i][j-1] 
        print(dp)            
        if dp[m][n] == m :
            return True
        return False
    
    
    def isSubsequence(self, s, t):
        if len(s) == 0 :
            return True
        j = -1
        for i in range(len(s)):  
            c = s[i]          
            while j < len(t):
                j += 1
                if j < len(t) and t[j] == c :
                    break              
            if i == len(s) - 1 and j != len(t) :
                return True
        return False    
                
        
    
ss = Solution()
s = "abc"; t = "ahbgdc"
print(ss.isSubsequence(s, t))
s = "axc"; t = "ahbgdc"
print(ss.isSubsequence(s, t))

