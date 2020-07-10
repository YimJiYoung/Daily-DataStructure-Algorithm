class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        counter = [0]*(len(nums)+1)
        for n in nums:
            counter[n]+=1
        for i in range(1, len(counter)):
            if counter[i] == 0:
                ans.append(i)
        return ans
        
        # Good Answer using space O(1)
        # # mark visited num negative
        # for i in range(len(nums)):
        #     temp = abs(nums[i]) - 1
        #     if (nums[temp] > 0):
        #         nums[temp]*=-1
        # # find unvisitied nums        
        # for i in range(len(nums)):
        #     if( nums[i] > 0):
        #         ans.append(i+1)
        # return ans