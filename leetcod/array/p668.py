# Nearly every one have used the Multiplication Table. But could you find out the k-th smallest number quickly from the multiplication table?
# 
# Given the height m and the length n of a m * n Multiplication Table, and a positive integer k, you need to return the k-th smallest number in this table.
# 
# Example 1:
# Input: m = 3, n = 3, k = 5
# Output: 
# Explanation: 
# The Multiplication Table:
# 1    2    3
# 2    4    6
# 3    6    9
# 
# The 5-th smallest number is 3 (1, 2, 2, 3, 3).
# Example 2:
# Input: m = 2, n = 3, k = 6
# Output: 
# Explanation: 
# The Multiplication Table:
# 1    2    3
# 2    4    6
# 
# The 6-th smallest number is 6 (1, 2, 2, 3, 4, 6).
# Note:
# The m and n will be in the range [1, 30000].
# The k will be in the range [1, m * n]

class Solution(object):
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: in
        :rtype: int
        """
#         matrix =  [ [(i+1)*(j+1) for i in range(m)]  for j in range(n)  ]
        
        lo = 1 #matrix[0][0]
        hi = m*n #matrix[-1][-1]
#         m = len(matrix)
        while lo < hi :
            mid = (lo + hi)/2
            count = 0;
            j = n-1
            for i in range(m) :
                while (i+1)*(j+1) > mid and j>=0  :
                    j -= 1
                count += j+1
            
            if count < k :
                lo = mid + 1
            else :
                hi = mid 
        
        return lo
    
    


s = Solution()

# m = 3
# n = 3
# k = 5        
# print s.findKthNumber(m,n , k)
# 
# m = 2
# n = 3
# k = 6        
# print s.findKthNumber(m,n , k)
# 
# m = 9895
# n = 28405
# k = 100787757        
# print s.findKthNumber(m,n , k)

m = 3
n = 1
k = 3        
print s.findKthNumber(m,n , k)
 