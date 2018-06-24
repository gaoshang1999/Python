# 697. Degree of an Array
# Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
# 
# Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
# 
# Example 1:
# Input: [1, 2, 2, 3, 1]
# Output: 2
# Explanation: 
# The input array has a degree of 2 because both elements 1 and 2 appear twice.
# Of the subarrays that have the same degree:
# [1, 2, 2, 3, 1], [1, 2, 2, 3], [2, 2, 3, 1], [1, 2, 2], [2, 2, 3], [2, 2]
# The shortest length is 2. So return 2.
# Example 2:
# Input: [1,2,2,3,1,4,2]
# Output: 6
# Note:
# 
# nums.length will be between 1 and 50,000.
# nums[i] will be an integer between 0 and 49,999.

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n =   max(nums) +1
        array = [[] for i in range(n)]
        
        mx = -1
        mxi = -1
        for i, x in enumerate(nums):
            a = array[x] 
            if len(a) == 0:
                array[x] = [1, i, i]
            else :
                array[x][0] += 1
                array[x][2] = i
                
            if(array[x][0] > mx) :
                mx = array[x][0]
                mxi = x
            elif array[x][0] == mx and array[x][2]-array[x][1] <  array[mxi][2]-array[mxi][1] :
                mxi = x
        
        print array
        print mxi
        print array[mxi]
        return array[mxi][2]-array[mxi][1]+1
    
s = Solution()
nums = [1, 2, 2, 3, 1]

print s.findShortestSubArray(nums)

nums = [1,2,2,3,1,4,2]

print s.findShortestSubArray(nums)

nums =[2,1,1,2,1,3,3,3,1,3,1,3,2]
print s.findShortestSubArray(nums)