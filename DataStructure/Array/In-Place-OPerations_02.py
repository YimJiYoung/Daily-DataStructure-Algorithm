# <Remove Duplicates from Sorted Array>
# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        uniq_length = 1
        for i in range(1, len(nums)):
            if (nums[i-1]!=nums[i]):
                nums[uniq_length]=nums[i]
                uniq_length+=1
        return uniq_length