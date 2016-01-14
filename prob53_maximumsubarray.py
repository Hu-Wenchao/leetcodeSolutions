"""
Find the contiguous subarray within an array (containing 
at least one number) which has the largest sum.

For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
the contiguous subarray [4,−1,2,1] has the largest sum = 6.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in xrange(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i-1])
        return max(nums)
