# Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        length = len(nums)
        largestSumOfSubArrayFrom = [0] * length
        largestSumOfSubArrayFrom[length - 1] = nums[length - 1]

        for i in reversed(range(length - 1)):
            largestSumOfSubArrayFrom[i] = max(
                largestSumOfSubArrayFrom[i + 1] + nums[i], nums[i])

        maxSum = -float('inf')

        for s in largestSumOfSubArrayFrom:
            maxSum = max(s, maxSum)

        return maxSum
