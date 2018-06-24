import copy

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
    def __str__(self):
        s = ""
        if self.left != None:
            s += self.left.__str__()
        s += " "+str(self.val)+ " "        
        if self.right != None:
            s += self.right.__str__()
        return s

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        
        dp[0] = 1
        for i in range(1, n+1):
            v = i//2
            for j in range(v):
                dp[i] += 2 * dp[j] * dp[i-1-j]
            if i%2 == 1 :
                dp[i] += dp[v] * dp[v]
        return dp
    
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        arr = [i for i in range(1, n+1)]
        return self.helper(arr, 0, n-1)

        
    def helper(self, arr, left, right):  
        if left > right :
            return [None]
        if left == right :
            return [TreeNode(arr[left])]      
        
        solutions = []
        for i in range(left, right+1):
            
            ls = self.helper(arr, left, i-1)
            rs = self.helper(arr, i+1, right)
            for a in ls:
                for b in rs:
                    t = TreeNode(arr[i])
                    t.left = a
                    t.right = b
                    solutions.append(t)
        return solutions
        
        
            
            
s = Solution()
print(s.numTrees(3))

print(s.numTrees(5))    


print(len(s.generateTrees(3)) )     
print(len(s.generateTrees(5)) )      