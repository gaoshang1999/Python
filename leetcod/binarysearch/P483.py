import math


class Solution:

    def smallestGoodBase(self, n):
        """
        :type n: str
        :rtype: str
        """
        n = int(n)

        def bsearch(lo, hi, f):
            if lo > hi: return None
            mid = (hi + lo) // 2
            val = f(mid)
            if val == 0: return mid
            elif val > 0: return bsearch(mid + 1, hi, f)
            else: return bsearch(lo, mid - 1, f)

        def key(b, ln):
            return sum(b ** i for i in range(ln))

        mxlen = int(math.log(n, 2) + 1)
        for ln in range(mxlen, 0, -1):
            b = bsearch(2, n, lambda x: n - key(x, ln))
            if b: return str(b)
        assert(False)      
        
    def convert(self, n, b):
        while n != 0:
            a = n % b
            if a != 1:
                return False
            n = n // b
        
        return True    

    
s = Solution()

print(s.convert(3, 2))
print(s.convert(13, 2))
print(s.convert(4681, 8))

print(s.smallestGoodBase(4681))
print(s.smallestGoodBase(1000000000000000000))
print(s.smallestGoodBase(936501597464173890))
