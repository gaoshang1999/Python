import heapq
import itertools


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        
        queue = []
        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs
    
s = Solution()

# nums1= [1,1,2]
# nums2=[1,2,3]
# k = 10
# 
# print s.kSmallestPairs(nums1, nums2, k)
# 
# nums1 = [1,7,11]; nums2 = [2,4,6];  k = 3
# print s.kSmallestPairs(nums1, nums2, k)
# 
# nums1 = [1,1,2]; nums2 = [1,2,3];  k = 2
# print s.kSmallestPairs(nums1, nums2, k)
# 
# nums1 = [1,2]; nums2 = [3];  k = 3 
# print s.kSmallestPairs(nums1, nums2, k)

nums1 =[1,2,4]
nums2 =[-1,1,2]
k=100

print s.kSmallestPairs(nums1, nums2, k)

