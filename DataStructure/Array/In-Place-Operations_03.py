# <Move Zeroes>
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        wi = 0
        for ri in range(len(nums)):
            if nums[ri] != 0:
                nums[wi] = nums[ri]
                wi += 1
    
        for i in range(wi, len(nums)):
            nums[i] = 0