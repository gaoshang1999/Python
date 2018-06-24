import collections

class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c  =collections.Counter(nums)
        return self.earn_dp(c)

    def earn(self, dt):
        if len(dt) == 0 :
            return 0
                
        mx = 0
        for k in dt :
            cp = dt.copy()
            del cp[k-1]
            del cp[k]
            del cp[k+1]
            v = self.earn(cp) + k * dt[k]
            if v > mx :
                mx = v
        return mx
    
    def earn_dp(self, dt):
        dp_2 = dp_1  = 0
        
        prv_k = -1
        for k in sorted(dt):
            v = k * dt[k]
            if k == prv_k +1 :
                dp = max(v + dp_2, dp_1)
            else :
                dp = dp_1 + v
                
            dp_2, dp_1 = dp_1, dp
            
            prv_k = k
        return dp_1


s = Solution();

nums = [3, 4, 2, 2]
print s.deleteAndEarn(nums)

nums = [3, 4, 2]
print s.deleteAndEarn(nums)

nums = [2, 2, 3, 3, 3, 4]
print s.deleteAndEarn(nums)

nums = [12,32,93,17,100,72,40,71,37,92,58,34,29,78,11,84,77,90,92,35,12,5,27,92,91,23,65,91,85,14,42,28,80,85,38,71,62,82,66,3,33,33,55,60,48,78,63,11,20,51,78,42,37,21,100,13,60,57,91,53,49,15,45,19,51,2,96,22,32,2,46,62,58,11,29,6,74,38,70,97,4,22,76,19,1,90,63,55,64,44,90,51,36,16,65,95,64,59,53,93]
print s.deleteAndEarn(nums)
