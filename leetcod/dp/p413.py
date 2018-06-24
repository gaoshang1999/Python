class Solution:
    def numberOfArithmeticSlices(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        cnt = 0
        n = len(A)
        for i in range(n):
            a = A[i]
            for j in range(i+1, min(i+2, n)):
                b = A[j]
                for k in range(j+1, n):
                    c = A[k]
                    if b - a == c - b :
                        a, b = b, c
                        cnt += 1
                    else:
                        break
        return cnt
    

s = Solution()
A = [1, 2, 3, 4]
print(s.numberOfArithmeticSlices(A))

A = [2,1,3,4,2,3]
print(s.numberOfArithmeticSlices(A))