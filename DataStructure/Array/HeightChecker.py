class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        count = 0
        sorted_heights = sorted(heights)
        for i in range(len(heights)):
            if sorted_heights[i] != heights[i]:
                count+=1
        return count

        #--- Using Coutting Sort ---#
        # ans = 0
        # heightsCount = [0]*101
        # cur = 0
        # for h in heights:
        #     heightsCount[h] += 1
        # for h in heights:
        #     while (heightsCount[cur] == 0):
        #         cur+=1
        #     if (cur != h) :
        #         ans+=1
        #     heightsCount[cur]-=1
        # return ans