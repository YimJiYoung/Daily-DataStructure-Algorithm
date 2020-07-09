class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        one, two, three = float('-inf'), float('-inf'), float('-inf')
        for v in nums:
            if v in [one, two, three]:
                continue
            if v > one : 
                one, two, three = v, one, two
            elif v > two :
                two, three = v, two
            elif v > three :
                three = v
        return three if three != float('-inf') else one